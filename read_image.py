import cv2
import os
import numpy as np

def read_and_return_images(folder_path):
    images = []  # List to store images

    # List all files in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is an image (you can add more extensions if needed)
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            # Read the image
            image = cv2.imread(file_path)
            
            if image is None:
                print(f"Error loading image: {file_path}")
                continue

            # Append the image to the list
            images.append(image)
            # print(f"Read: {file_path}")

    return images