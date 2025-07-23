# utils/sharpen.py
import cv2
import numpy as np

def sharpen_image(image: np.ndarray, intensity: float = 1.0) -> np.ndarray:
    # Basic sharpening kernel with controlled intensity
    kernel = np.array([[0, -1, 0],
                       [-1, 5 + intensity, -1],
                       [0, -1, 0]])

    # Apply kernel
    sharpened = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

    # Clip values to prevent brightness overflow
    sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
    return sharpened
