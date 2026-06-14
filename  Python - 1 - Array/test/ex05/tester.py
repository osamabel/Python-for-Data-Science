import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex05"))

from pimp_image import (  # noqa: E402
    ft_invert, ft_red, ft_green, ft_blue, ft_grey
)


def make_arr(r, g, b):
    """Create a tiny 2x2 RGB array with fixed channel values."""
    arr = np.zeros((2, 2, 3), dtype=np.uint8)
    arr[:, :, 0] = r
    arr[:, :, 1] = g
    arr[:, :, 2] = b
    return arr


def test_invert_values():
    """ft_invert: each value becomes 255 - original."""
    arr = make_arr(100, 150, 200)
    result = ft_invert(arr)
    assert result[0, 0, 0] == 155, f"Expected 155, got {result[0,0,0]}"
    assert result[0, 0, 1] == 105, f"Expected 105, got {result[0,0,1]}"
    assert result[0, 0, 2] == 55, f"Expected 55, got {result[0,0,2]}"
    print("test_invert_values passed")


def test_invert_shape():
    """ft_invert keeps the original shape."""
    arr = np.random.randint(0, 255, (10, 20, 3), dtype=np.uint8)
    assert ft_invert(arr).shape == arr.shape
    print("test_invert_shape passed")


def test_red_channels():
    """ft_red: G and B channels become 0, R is unchanged."""
    arr = make_arr(120, 80, 60)
    result = ft_red(arr)
    assert result[0, 0, 0] == 120, "R channel should be unchanged"
    assert result[0, 0, 1] == 0, "G channel should be zeroed"
    assert result[0, 0, 2] == 0, "B channel should be zeroed"
    print("test_red_channels passed")


def test_green_channels():
    """ft_green: R and B channels become 0, G is unchanged."""
    arr = make_arr(120, 80, 60)
    result = ft_green(arr)
    assert result[0, 0, 0] == 0, "R channel should be zeroed"
    assert result[0, 0, 1] == 80, "G channel should be unchanged"
    assert result[0, 0, 2] == 0, "B channel should be zeroed"
    print("test_green_channels passed")


def test_blue_channels():
    """ft_blue: R and G channels become 0, B is unchanged."""
    arr = make_arr(120, 80, 60)
    result = ft_blue(arr)
    assert result[0, 0, 0] == 0, "R channel should be zeroed"
    assert result[0, 0, 1] == 0, "G channel should be zeroed"
    assert result[0, 0, 2] == 60, "B channel should be unchanged"
    print("test_blue_channels passed")


def test_grey_equal_channels():
    """ft_grey: all 3 channels must be equal (grayscale)."""
    arr = make_arr(90, 60, 30)
    result = ft_grey(arr)
    assert result[0, 0, 0] == result[0, 0, 1] == result[0, 0, 2], (
        "Grey filter must produce equal R, G, B channels"
    )
    print("test_grey_equal_channels passed")


def test_grey_value():
    """ft_grey: channel value is approximately (R+G+B)/3."""
    arr = make_arr(90, 60, 30)
    result = ft_grey(arr)
    expected = (90 + 60 + 30) // 3
    assert abs(int(result[0, 0, 0]) - expected) <= 1, (
        f"Expected ~{expected}, got {result[0,0,0]}"
    )
    print("test_grey_value passed")


def test_all_shapes_preserved():
    """All filters must return an array with the same shape as input."""
    arr = np.random.randint(0, 255, (30, 50, 3), dtype=np.uint8)
    for fn in [ft_invert, ft_red, ft_green, ft_blue, ft_grey]:
        result = fn(arr)
        assert result.shape == arr.shape, (
            f"{fn.__name__} changed shape: {result.shape} != {arr.shape}"
        )
    print("test_all_shapes_preserved passed")


def test_docstrings_exist():
    """All filter functions must have a docstring."""
    for fn in [ft_invert, ft_red, ft_green, ft_blue, ft_grey]:
        assert fn.__doc__, f"{fn.__name__} is missing a docstring"
    print("test_docstrings_exist passed")


def main():
    """Run all ex05 tests."""
    print("=" * 50)
    print("Filter value tests:")
    test_invert_values()
    test_invert_shape()
    test_red_channels()
    test_green_channels()
    test_blue_channels()
    test_grey_equal_channels()
    test_grey_value()
    print()
    print("=" * 50)
    print("Shape and docstring tests:")
    test_all_shapes_preserved()
    test_docstrings_exist()


if __name__ == "__main__":
    main()
