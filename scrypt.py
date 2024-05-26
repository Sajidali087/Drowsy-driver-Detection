import cv2
import os
from PIL import Image
import numpy as np
from image_resize import resize_images
from save_images import save_images
from read_image import read_and_return_images
from greyScale import convert_to_grayscale
from histogram_equi import adaptive_histogram_equalization

folder_path = "Drowsiness Detection.v2-augmented-v1.yolov5pytorch/valid/images"
# folderPath =  "image"

# extracting original file names
output_folder='image'
original_filenames=[]
filenames = os.listdir(folder_path)
for filename in filenames:
    img_path = os.path.join(folder_path, filename)
    img = Image.open(img_path)
    original_filenames.append(filename)

# Function calling
images =    read_and_return_images(folder_path)
imageResized = resize_images(images)
grayScaleImage = convert_to_grayscale(imageResized)
# print(type(grayScaleImage))
# print(grayScaleImage.shape)
equilized_Image = adaptive_histogram_equalization(grayScaleImage)
processed_image = [Image.fromarray(img) for img in equilized_Image]
# filtered_image = apply_butterworth_high_pass_filter_to_list(equilized_Image)
save_images(processed_image, original_filenames, output_folder)



# Reading the returned images outside the function
for idx, image in enumerate(equilized_Image):
    # Example: Display the images
    # print(idx)
    # if idx%5==0:
    cv2.imshow(original_filenames[idx], image)
    print(type(image))
    print(image.shape)
    key = cv2.waitKey(0)

        # If the 'q' key is pressed, destroy all windows and exit
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    cv2.destroyAllWindows()
