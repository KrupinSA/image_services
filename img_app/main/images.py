from os import path
import os, datetime
from flask import current_app
import shutil


def get_image_work_path(name:str)->str:
    img_dir = current_app.config['IMAGE_DIR']
    return path.join(img_dir, name)


def get_names(img_dir) -> list:
    '''
    Возвращает спикок кортежей (имя файла, дата создания)
    '''
    names = []
    for name in os.listdir(img_dir):
        full_path = get_image_work_path(name)
        if path.isfile(full_path):
            created = os.path.getctime(full_path)
            date = datetime.datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M:%S")
            name_with_date = name, date
            names.append(name_with_date)
   
    return names


def copy_images(resource_dir):
    for name in os.listdir(resource_dir):
        shutil.copyfile(path.join(resource_dir, name), get_image_work_path(name))


