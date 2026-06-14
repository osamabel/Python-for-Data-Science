import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex01"))

from array2D import slice_me  # noqa: E402


def test_subject_example():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


def test_returns_list():
    family = [[1, 2], [3, 4], [5, 6]]
    result = slice_me(family, 0, 2)
    assert isinstance(result, list), f"Expected list, got {type(result)}"
    assert isinstance(result[0], list), "Expected list of lists"
    print("test_returns_list passed")


def test_full_slice():
    family = [[1, 2], [3, 4], [5, 6]]
    result = slice_me(family, 0, 3)
    assert len(result) == 3, f"Expected 3 rows, got {len(result)}"
    print("test_full_slice passed")


def test_negative_index():
    family = [[1, 2], [3, 4], [5, 6], [7, 8]]
    result = slice_me(family, 1, -1)
    assert len(result) == 2, f"Expected 2 rows, got {len(result)}"
    print("test_negative_index passed")


def test_empty_slice():
    family = [[1, 2], [3, 4]]
    result = slice_me(family, 2, 2)
    assert result == [], f"Expected [], got {result}"
    print("test_empty_slice passed")


def test_error_not_a_list():
    result = slice_me("not a list", 0, 1)
    assert result is None, f"Expected None, got {result}"
    print("test_error_not_a_list passed")


def test_error_1d_array():
    result = slice_me([1, 2, 3], 0, 2)
    assert result is None, f"Expected None, got {result}"
    print("test_error_1d_array passed")


def test_error_non_int_bounds():
    family = [[1, 2], [3, 4]]
    result = slice_me(family, 0.0, 1.0)
    assert result is None, f"Expected None, got {result}"
    print("test_error_non_int_bounds passed")


def main():
    print("=" * 50)
    print("Subject example:")
    test_subject_example()
    print()
    print("=" * 50)
    print("Unit tests:")
    test_returns_list()
    test_full_slice()
    test_negative_index()
    test_empty_slice()
    print()
    print("=" * 50)
    print("Error handling tests:")
    test_error_not_a_list()
    test_error_1d_array()
    test_error_non_int_bounds()


if __name__ == "__main__":
    main()
