import os
import numpy as np
from PIL import Image

def save_images(processed_images, original_filenames, output_folder):
    """
    Save processed images to the specified output folder with their original filenames.

    Parameters:
    processed_images (list of PIL.Image.Image): List of processed images.
    original_filenames (list of str): List of original filenames corresponding to each image.
    output_folder (str): The folder where images will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for img, filename in zip(processed_images, original_filenames):
        save_path = os.path.join(output_folder, filename)
        img.save(save_path)

    print(f"All images have been saved to {output_folder}.")
