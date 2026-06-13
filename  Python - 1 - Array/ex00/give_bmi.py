import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    """Calculate BMI for each pair of height and weight values."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Arguments must be lists")
    if len(height) != len(weight):
        raise ValueError("Lists must be the same size")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("List elements must be int or float")
        if h <= 0:
            raise ValueError("Height must be strictly positive")
        if w <= 0:
            raise ValueError("Weight must be strictly positive")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value that exceeds the given limit."""
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if not isinstance(limit, int):
        raise TypeError("limit must be an int")
    arr = np.array(bmi, dtype=float)
    return (arr > limit).tolist()


def main():
    """Test give_bmi and apply_limit with sample data."""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
