import os

import PIL
from PIL import Image
from io import BytesIO
import requests


def download_photo(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            img = Image.open(BytesIO(response.content))
            img.save(file_path)
            print("Photo downloaded successfully!")
        except PIL.UnidentifiedImageError:
            print("Failed to identify the image file.")
    else:
        print("Failed to download photo.")

def delete_photo(file_path):
    # Specify the path of the file to be deleted

    if os.path.exists(file_path) and file_path.endswith(".jpg"):
        # Delete the file
        os.remove(file_path)
        print("JPG file deleted successfully.")
    else:
        print("JPG file does not exist.")
