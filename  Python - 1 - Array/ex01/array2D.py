import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be integers")
        arr = np.array(family)
        if arr.ndim != 2:
            raise ValueError("family must be a 2D list (all rows same length)")
        print(f"My shape is : {arr.shape}")
        sliced = arr[start:end]
        print(f"My new shape is : {sliced.shape}")
        return sliced.tolist()
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
