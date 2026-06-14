import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(arr: np.ndarray) -> np.ndarray:
    """Slice a 400x400 region and convert to single-channel grayscale."""
    try:
        if not isinstance(arr, np.ndarray):
            raise TypeError("arr must be a numpy array")
        sliced = arr[200:600, 300:700]
        grey = sliced.mean(axis=2).astype(np.uint8)
        return grey
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


def rotate(arr: np.ndarray) -> np.ndarray:
    """Rotate a 2D array 90 degrees clockwise manually."""
    try:
        if not isinstance(arr, np.ndarray):
            raise TypeError("arr must be a numpy array")
        if arr.ndim != 2:
            raise ValueError("arr must be a 2D array")
        rows, cols = arr.shape
        result = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(arr[i, j])
            result.append(new_row)
        return np.array(result)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


def main():
    arr = ft_load("animal.jpeg")
    if arr is None:
        return
    zoomed = zoom_image(arr)
    if zoomed is None:
        return
    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed)
    transposed = rotate(zoomed)
    if transposed is None:
        return
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    plt.imshow(transposed, cmap='gray')
    plt.title("Transposed Image")
    plt.show()


if __name__ == "__main__":
    main()
