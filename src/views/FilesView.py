from flask_restful import Resource
from flask import send_file
from .. import main

class ItemFile(Resource):
    ''' Работаем с текущим файлом'''

    def get(self, file_name):
        '''
        Download file with file_name
        GET /api/v1.0/file/<string:file_name>
        '''
        return send_file(main.images.get_image_path(file_name))