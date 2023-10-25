import os
from django_config.settings import BASE_DIR

def delete_images(image:str):
    try:
        os.remove(str(BASE_DIR)+image)
    except:
        pass