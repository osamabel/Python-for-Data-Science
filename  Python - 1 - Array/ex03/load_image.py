import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load a JPG image and return it as an RGB numpy array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Only JPG/JPEG formats are supported")
        img = Image.open(path).convert('RGB')
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        return arr
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")


def main():
    ft_load("landscape.jpg")


if __name__ == "__main__":
    main()
