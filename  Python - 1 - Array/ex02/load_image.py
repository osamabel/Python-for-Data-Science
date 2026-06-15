import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load a JPG image, print its shape, return it as an RGB numpy array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Only JPG/JPEG formats are supported")
        img = Image.open(path)
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        return arr
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")


def main():
    """Test ft_load with landscape.jpg."""
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
