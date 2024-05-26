import cv2
import os
import numpy as np

def convert_to_grayscale(images):
    grayscale_images = []  # List to store grayscale images

    # Iterate over each image in the input list
    for image in images:
        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Append the grayscale image to the list
        grayscale_images.append(grayscale_image)

    return grayscale_images