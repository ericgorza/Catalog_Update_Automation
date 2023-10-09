## PROCESSES THE TXT FILES AND SAVE THEM AS JSON SO WE CAN UPLOAD IT TO THE WEBSITE ##

import requests
import os

#Find text paths:

txt_directory = "supplier-data/descriptions/"
txt_files = os.listdir(txt_directory)
txt_paths = [txt_directory + f for f in txt_files if f.endswith(".txt")]
#Define the URL:

URL = "http://34.27.93.204/fruits"

def getElement(file):
    # Find IDs to set the image name:
    entry_id = os.path.splitext(file)[0]
    img_name = entry_id+".jpeg"

    with open(file) as f:
      content = f.readlines()
      name = content[0].strip("\n")
      weight = int(content[1].strip('lbs \n'))
      description = content[2]

## Creating a List of Dictionaries with the txt information

    keys = ["name","weight","description","img_name"]
    values = [name,weight,description,img_name]
    dict_element = dict(zip(keys,values))
    return dict_element


#Posting it:

for txt_file in txt_paths:
    data = getElement(txt_file)
    response = requests.post(data,url=URL)
    if response.ok:
        print("Posted!")
    else:
        print(f"ERROR: {response.status_code}")


