## PROCESSES THE IMAGES ## - CORRIGIR

# Import the modules that we're gonna use

import os
from PIL import Image

## Localize the files:

img_directory = "/supplier-data/images" #your directory with images. (~/supplier-data/images)

img_files = os.listdir(img_directory)

image_format = ".jpg" #image format
wanted_format = "JPEG" #the format that you want

images_list = [img for img in img_files if img.endswith(".tiff")]

# Change all the images:
for file in images_list:
    source_img = Image.open(img_directory + file)
    new_img = source_img.resize(600,400)
    new_img = new_img.convert("RGB")
    file, ext = os.path.splitext(file)
    file += ".jpeg"
    new_img.save(img_directory + file, wanted_format)