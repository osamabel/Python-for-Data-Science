import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex00"))

from give_bmi import give_bmi, apply_limit  # noqa: E402


def test_subject_example():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def test_all_below_limit():
    bmi = give_bmi([1.75, 1.80], [60.0, 65.0])
    result = apply_limit(bmi, 30)
    assert result == [False, False], f"Expected [False, False], got {result}"
    print("test_all_below_limit passed")


def test_all_above_limit():
    bmi = give_bmi([1.50, 1.60], [120.0, 130.0])
    result = apply_limit(bmi, 25)
    assert result == [True, True], f"Expected [True, True], got {result}"
    print("test_all_above_limit passed")


def test_integer_inputs():
    bmi = give_bmi([2, 1], [80, 50])
    assert len(bmi) == 2
    assert isinstance(bmi[0], float)
    print("test_integer_inputs passed")


def test_single_element():
    bmi = give_bmi([1.75], [70.0])
    expected = 70.0 / (1.75 ** 2)
    assert abs(bmi[0] - expected) < 1e-9, f"Expected {expected}, got {bmi[0]}"
    print("test_single_element passed")


def test_return_types():
    bmi = give_bmi([1.75], [70.0])
    assert isinstance(bmi, list), "give_bmi must return a list"
    limits = apply_limit(bmi, 20)
    assert isinstance(limits, list), "apply_limit must return a list"
    assert type(limits[0]) is bool, "elements must be plain Python bool"
    print("test_return_types passed")


def test_error_mismatched_sizes():
    result = give_bmi([1.75, 1.80], [70.0])
    assert result is None, f"Expected None, got {result}"
    print("test_error_mismatched_sizes passed")


def test_error_not_a_list():
    result = give_bmi((1.75,), [70.0])
    assert result is None, f"Expected None, got {result}"
    print("test_error_not_a_list passed")


def test_error_non_numeric_element():
    result = give_bmi([1.75, "tall"], [70.0, 80.0])
    assert result is None, f"Expected None, got {result}"
    print("test_error_non_numeric_element passed")


def test_error_zero_height():
    result = give_bmi([0.0, 1.75], [70.0, 70.0])
    assert result is None, f"Expected None, got {result}"
    print("test_error_zero_height passed")


def test_error_zero_weight():
    result = give_bmi([1.75, 1.80], [70.0, 0.0])
    assert result is None, f"Expected None, got {result}"
    print("test_error_zero_weight passed")


def test_error_negative_weight():
    result = give_bmi([1.75], [-70.0])
    assert result is None, f"Expected None, got {result}"
    print("test_error_negative_weight passed")


def test_error_limit_not_int():
    result = apply_limit([22.5, 30.0], 25.5)
    assert result is None, f"Expected None, got {result}"
    print("test_error_limit_not_int passed")


def main():
    print("=" * 50)
    print("Subject example:")
    test_subject_example()
    print()
    print("=" * 50)
    print("Unit tests:")
    test_all_below_limit()
    test_all_above_limit()
    test_integer_inputs()
    test_single_element()
    test_return_types()
    print()
    print("=" * 50)
    print("Error handling tests:")
    test_error_mismatched_sizes()
    test_error_not_a_list()
    test_error_non_numeric_element()
    test_error_zero_height()
    test_error_zero_weight()
    test_error_negative_weight()
    test_error_limit_not_int()


if __name__ == "__main__":
    main()
