from os import path
import os, datetime
from flask import current_app


def get_names() -> list:
    img_dir = current_app.config['IMAGE_DIR']
    names = []
    for name in os.listdir(img_dir):
        full_path = path.join(img_dir, name)
        if path.isfile(full_path):
            created = os.path.getctime(full_path)
            date = datetime.datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M:%S")
            name_with_date = name, date
            names.append(name_with_date)
   
    return names


def get_image_path(name:str)->str:
    img_dir = current_app.config['IMAGE_DIR']
    return path.join(img_dir, name)