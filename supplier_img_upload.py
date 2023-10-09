## POST IMAGES ON THE WEBSITE -

# Import Modules
import requests
from os import listdir

#Define Path and URL

img_directory = "supplier-data/images"
url = "http://localhost/upload/"

#Define POST function:

def upload_img(file,url):
    with open(file, "rb") as file:
        requests.post(url=url, files={"file":file})

#Make a list of images paths:

img_paths_list = [img_directory + img for img in listdir(img_directory) if img.endswith(".jpeg")]

#Call the function for each image:

for image in img_paths_list:
    upload_img(image,url)

