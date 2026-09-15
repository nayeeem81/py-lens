from pathlib import Path

import numpy as np
from PIL import Image


DEFAULT_IMAGE = Path(__file__).with_name("sample.png")


def create_sample_image(path: Path = DEFAULT_IMAGE) -> Path:
    """Create a small RGB test image when no source image has been supplied."""
    height, width = 96, 144
    y, x = np.mgrid[0:height, 0:width]
    red = (x / (width - 1) * 255).astype(np.uint8)
    green = (y / (height - 1) * 255).astype(np.uint8)
    blue = (((x + y) / (width + height - 2)) * 255).astype(np.uint8)
    tensor = np.stack((red, green, blue), axis=-1)
    Image.fromarray(tensor, mode="RGB").save(path)
    return path


def load_rgb_tensor(path: Path = DEFAULT_IMAGE) -> np.ndarray:
    """Load an image as an H x W x 3 uint8 RGB tensor."""
    if not path.exists():
        create_sample_image(path)
    with Image.open(path) as image:
        return np.asarray(image.convert("RGB"), dtype=np.uint8).copy()


def tensor_payload(tensor: np.ndarray) -> dict:
    """Convert the tensor into JSON-friendly data for the canvas."""
    height, width, channels = tensor.shape
    if channels != 3:
        raise ValueError("Expected an RGB tensor with three channels")
    return {
        "width": width,
        "height": height,
        "channels": ["r", "g", "b"],
        "pixels": tensor.tolist(),
    }
