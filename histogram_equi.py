import cv2
import os
import numpy as np

def adaptive_histogram_equalization(images):
    """
    Apply Adaptive Histogram Equalization (AHE) to a list of grayscale images.
    
    Args:
    - images: List of input grayscale images (list of numpy arrays).
    
    Returns:
    - List of equalized images (list of numpy arrays).
    """
    # Initialize an empty list to store the equalized images
    equalized_images = []
    
    # Apply adaptive histogram equalization to each image in the list
    for image in images:
        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        equalized_image = clahe.apply(image)
        
        # Append the equalized image to the list
        equalized_images.append(equalized_image)
    
    return equalized_images