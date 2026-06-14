import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex04"))

from rotate import manual_transpose, zoom_image  # noqa: E402


def test_square_shape_unchanged():
    """Transposing a square 2D array keeps the same shape."""
    arr = np.random.randint(0, 255, (400, 400), dtype=np.uint8)
    result = manual_transpose(arr)
    assert result.shape == (400, 400), (
        f"Expected (400, 400), got {result.shape}"
    )
    print("test_square_shape_unchanged passed")


def test_non_square_shape():
    """Transposing (3, 5) must produce (5, 3)."""
    arr = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15]])
    result = manual_transpose(arr)
    assert result.shape == (5, 3), f"Expected (5, 3), got {result.shape}"
    print("test_non_square_shape passed")


def test_values_are_correct():
    """result[j][i] must equal original[i][j]."""
    arr = np.array([[1, 2, 3],
                    [4, 5, 6]])
    result = manual_transpose(arr)
    assert result[0, 0] == 1
    assert result[1, 0] == 2
    assert result[2, 0] == 3
    assert result[0, 1] == 4
    assert result[2, 1] == 6
    print("test_values_are_correct passed")


def test_double_transpose_identity():
    """Transposing twice must yield the original array."""
    arr = np.random.randint(0, 255, (10, 20), dtype=np.uint8)
    result = manual_transpose(manual_transpose(arr))
    assert np.array_equal(result, arr), "Double transpose must equal original"
    print("test_double_transpose_identity passed")


def test_zoom_feeds_into_transpose():
    """zoom_image output (400,400,1) squeezed to 2D is valid transpose input."""
    source = np.random.randint(0, 255, (768, 1024, 3), dtype=np.uint8)
    zoomed = zoom_image(source)
    flat = zoomed[:, :, 0]
    result = manual_transpose(flat)
    assert result.shape == (400, 400)
    print("test_zoom_feeds_into_transpose passed")


def test_uses_no_library_transpose():
    """Verify rotate.py source does not call numpy transpose methods."""
    rotate_path = os.path.join(
        os.path.dirname(__file__), "../../ex04/rotate.py"
    )
    with open(rotate_path) as f:
        src = f.read()
    forbidden = ['.T ', '.T\n', '.T)', 'np.transpose', 'np.swapaxes']
    for token in forbidden:
        assert token not in src, (
            f"Found forbidden transpose method '{token}' in rotate.py"
        )
    print("test_uses_no_library_transpose passed")


def main():
    """Run all ex04 tests."""
    print("=" * 50)
    print("Unit tests (manual_transpose):")
    test_square_shape_unchanged()
    test_non_square_shape()
    test_values_are_correct()
    test_double_transpose_identity()
    test_zoom_feeds_into_transpose()
    test_uses_no_library_transpose()


if __name__ == "__main__":
    main()
