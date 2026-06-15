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


def main():
    """Load animal.jpeg, zoom into a region, and display it."""
    arr = ft_load("animal.jpeg")
    print(arr)
    if arr is None:
        return
    zoomed = zoom_image(arr)
    if zoomed is None:
        return
    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)
    plt.imshow(zoomed, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
