import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ex00"))

from give_bmi import give_bmi, apply_limit  # noqa: E402


def test_subject_example():
    """Subject tester: matches the expected output exactly."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def test_all_below_limit():
    """All BMI values are below the limit — all False."""
    bmi = give_bmi([1.75, 1.80], [60.0, 65.0])
    result = apply_limit(bmi, 30)
    assert result == [False, False], f"Expected [False, False], got {result}"
    print("test_all_below_limit passed")


def test_all_above_limit():
    """All BMI values exceed the limit — all True."""
    bmi = give_bmi([1.50, 1.60], [120.0, 130.0])
    result = apply_limit(bmi, 25)
    assert result == [True, True], f"Expected [True, True], got {result}"
    print("test_all_above_limit passed")


def test_integer_inputs():
    """give_bmi accepts integers as well as floats."""
    bmi = give_bmi([2, 1], [80, 50])
    assert len(bmi) == 2
    assert isinstance(bmi[0], float)
    print("test_integer_inputs passed")


def test_single_element():
    """Single-element lists work correctly."""
    bmi = give_bmi([1.75], [70.0])
    expected = 70.0 / (1.75 ** 2)
    assert abs(bmi[0] - expected) < 1e-9, f"Expected {expected}, got {bmi[0]}"
    print("test_single_element passed")


def test_error_mismatched_sizes():
    """Different-length lists must raise ValueError."""
    try:
        give_bmi([1.75, 1.80], [70.0])
        print("FAIL: expected ValueError")
    except ValueError as e:
        print(f"test_error_mismatched_sizes passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_error_not_a_list():
    """Non-list arguments must raise TypeError."""
    try:
        give_bmi((1.75,), [70.0])
        print("FAIL: expected TypeError")
    except TypeError as e:
        print(f"test_error_not_a_list passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_error_non_numeric_element():
    """String elements in the list must raise TypeError."""
    try:
        give_bmi([1.75, "tall"], [70.0, 80.0])
        print("FAIL: expected TypeError")
    except TypeError as e:
        print(f"test_error_non_numeric_element passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_error_zero_height():
    """Zero height must raise ValueError (division by zero)."""
    try:
        give_bmi([0.0, 1.75], [70.0, 70.0])
        print("FAIL: expected ValueError")
    except ValueError as e:
        print(f"test_error_zero_height passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_error_zero_weight():
    """Zero or negative weight must raise ValueError."""
    try:
        give_bmi([1.75, 1.80], [70.0, 0.0])
        print("FAIL: expected ValueError")
    except ValueError as e:
        print(f"test_error_zero_weight passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_error_negative_weight():
    """Negative weight must raise ValueError."""
    try:
        give_bmi([1.75], [-70.0])
        print("FAIL: expected ValueError")
    except ValueError as e:
        print(f"test_error_negative_weight passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_error_limit_not_int():
    """apply_limit must raise TypeError if limit is not an int."""
    try:
        apply_limit([22.5, 30.0], 25.5)
        print("FAIL: expected TypeError")
    except TypeError as e:
        print(f"test_error_limit_not_int passed: {e}")
    except Exception as e:
        print(f"FAIL: unexpected exception: {e}")


def test_return_types():
    """give_bmi returns list of floats, apply_limit returns list of bools."""
    bmi = give_bmi([1.75], [70.0])
    assert isinstance(bmi, list), "give_bmi must return a list"
    limits = apply_limit(bmi, 20)
    assert isinstance(limits, list), "apply_limit must return a list"
    assert type(limits[0]) is bool, "elements must be plain Python bool"
    print("test_return_types passed")


def main():
    """Run all ex00 tests."""
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
