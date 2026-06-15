import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex03"))

from zoom import zoom_image  # noqa: E402

TEST_IMG = os.path.join(os.path.dirname(__file__), "test_animal.jpeg")


def make_test_image():
    """Create a synthetic 768x1024 JPEG large enough to zoom into."""
    from PIL import Image
    arr = np.random.randint(0, 255, (768, 1024, 3), dtype=np.uint8)
    img = Image.fromarray(arr, 'RGB')
    img.save(TEST_IMG, 'JPEG')


def test_zoom_output_shape():
    arr = np.random.randint(0, 255, (768, 1024, 3), dtype=np.uint8)
    zoomed = zoom_image(arr)
    assert zoomed.shape == (400, 400), (
        f"Expected (400, 400), got {zoomed.shape}"
    )
    print("test_zoom_output_shape passed")


def test_zoom_dtype():
    arr = np.random.randint(0, 255, (768, 1024, 3), dtype=np.uint8)
    zoomed = zoom_image(arr)
    assert zoomed.dtype == np.uint8, f"Expected uint8, got {zoomed.dtype}"
    print("test_zoom_dtype passed")


def test_zoom_values_in_range():
    arr = np.random.randint(0, 255, (768, 1024, 3), dtype=np.uint8)
    zoomed = zoom_image(arr)
    assert zoomed.min() >= 0 and zoomed.max() <= 255
    print("test_zoom_values_in_range passed")


def test_zoom_is_greyscale():
    arr = np.zeros((768, 1024, 3), dtype=np.uint8)
    arr[200:600, 300:700, 0] = 90
    arr[200:600, 300:700, 1] = 60
    arr[200:600, 300:700, 2] = 30
    zoomed = zoom_image(arr)
    expected = int(round((90 + 60 + 30) / 3))
    assert abs(int(zoomed[0, 0]) - expected) <= 1, (
        f"Expected ~{expected}, got {zoomed[0, 0]}"
    )
    print("test_zoom_is_greyscale passed")


def main():
    """Run all ex03 tests."""
    print("=" * 50)
    print("Unit tests (zoom_image):")
    test_zoom_output_shape()
    test_zoom_dtype()
    test_zoom_values_in_range()
    test_zoom_is_greyscale()
    if os.path.exists(TEST_IMG):
        os.remove(TEST_IMG)


if __name__ == "__main__":
    main()
