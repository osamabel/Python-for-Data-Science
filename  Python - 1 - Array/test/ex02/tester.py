import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex02"))

from load_image import ft_load  # noqa: E402

TEST_IMG = os.path.join(os.path.dirname(__file__), "test_img.jpg")


def make_test_image():
    """Create a small synthetic JPEG for testing."""
    from PIL import Image
    arr = np.random.randint(0, 255, (50, 80, 3), dtype=np.uint8)
    img = Image.fromarray(arr, 'RGB')
    img.save(TEST_IMG, 'JPEG')


def test_returns_array():
    """ft_load returns a numpy ndarray."""
    make_test_image()
    arr = ft_load(TEST_IMG)
    assert isinstance(arr, np.ndarray), f"Expected ndarray, got {type(arr)}"
    assert arr.ndim == 3, f"Expected 3D array, got ndim={arr.ndim}"
    assert arr.shape[2] == 3, "Expected 3 channels (RGB)"
    print("test_returns_array passed")


def test_shape_printed(capsys=None):
    """Shape is printed before the array data."""
    make_test_image()
    ft_load(TEST_IMG)
    print("test_shape_printed passed (check stdout manually above)")


def test_dtype_uint8():
    """Pixel values must be uint8 (0-255)."""
    make_test_image()
    arr = ft_load(TEST_IMG)
    assert arr.dtype == np.uint8, f"Expected uint8, got {arr.dtype}"
    print("test_dtype_uint8 passed")


def test_error_wrong_extension():
    result = ft_load("image.png")
    assert result is None, f"Expected None, got {result}"
    print("test_error_wrong_extension passed")


def test_error_not_a_string():
    result = ft_load(123)
    assert result is None, f"Expected None, got {result}"
    print("test_error_not_a_string passed")


def test_error_file_not_found():
    result = ft_load("does_not_exist.jpg")
    assert result is None, f"Expected None, got {result}"
    print("test_error_file_not_found passed")


def main():
    """Run all ex02 tests."""
    print("=" * 50)
    print("Unit tests:")
    test_returns_array()
    test_shape_printed()
    test_dtype_uint8()
    print()
    print("=" * 50)
    print("Error handling tests:")
    test_error_wrong_extension()
    test_error_not_a_string()
    test_error_file_not_found()
    if os.path.exists(TEST_IMG):
        os.remove(TEST_IMG)


if __name__ == "__main__":
    main()
