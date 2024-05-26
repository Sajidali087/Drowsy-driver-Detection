import cv2
import os
import numpy as np
# Function to resize the images
def resize_images(images, size=(320, 320)):
    """
    Resize a list of images to the specified size.

    Parameters:
    images (list): List of images (as NumPy arrays) to be resized.
    size (tuple): Target size for resizing the images (width, height).

    Returns:
    list: List of resized images.
    """
    resized_images = []
    
    for image in images:
        # Resize the image
        resized_image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
        # Append the resized image to the list
        resized_images.append(resized_image)
    
    return resized_images
