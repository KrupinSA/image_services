from flask_restful import Resource, url_for, reqparse
from flask import current_app
import sqlite3 
import werkzeug
import datetime
import os
from .. import main

parser = reqparse.RequestParser()
parser.add_argument('file',
                    type=werkzeug.datastructures.FileStorage,
                    location='files',
                    required=True,
                    )
parser.add_argument('text')

class ItemImage(Resource):
    ''' Работаем с текущей картинкой'''


    def comm_to_json(self, comm:tuple)->dict:
        id, comm = comm
        return {'comm': comm,
                'comm_url': url_for('bp.itemcomments', comment_id=id)
               }


    def get(self, image_id):
        '''
        Get comments collection for image id 
        GET /api/v1.0/images/<int:image_id>/comments
        '''
        db = main.db.get_db()
        checked_id = db.execute('SELECT id FROM image WHERE id=?', (image_id,)).fetchall()
        if checked_id:
            comments = db.execute('SELECT id, text FROM comment WHERE image_id=?',
                                 (image_id,)).fetchall()
            return {'comments': [self.comm_to_json(comm) for comm in comments],
                    'img_url': url_for('bp.aboutimage', image_id=image_id)
                    }
        return {'message': 'Image not found'}, 404
        

    def post(self, image_id):
        '''
        Add new comments for image id
        POST /api/v1.0/images/<int:image_id>/comments
        '''
        args = parser.parse_args()
        db = main.db.get_db()
        if not args['text']: return {'message': 'Empty comment'}, 400 
        checked_id = db.execute('SELECT id FROM image WHERE id=?', (image_id,)).fetchall()
        if checked_id:
            try:
                db.execute('INSERT INTO comment (text, image_id) VALUES (?, ?)',
                            (args['text'], image_id))
                db.commit()
                return {'message':'Comment append'}, 201
            except sqlite3.Error as error:
                return {'message': error}, 500
        return {'message': 'Image not found'}, 404

            
class ImagesList(Resource):
    '''Работаем с коллекцией картинок'''

    def image_to_json(self, img:tuple)->dict:
        id, name, date = img
        return {'name': name,
                'time': date.strftime("%Y-%m-%d %H:%M:%S"),
                'file_url': url_for('bp.itemfile', file_name=name),
                'comm_url': url_for('bp.itemimage', image_id=id)
               }
            

    def get(self):
        ''' 
        Get collection name of images
        GET /api/v1.0/images
        '''
        db = main.db.get_db()
        images = db.execute('SELECT id, name, date FROM image').fetchall()
        return {'images': [self.image_to_json(img) for img in images]}                


    def post(self):
        '''
        Add new image to collection
        POST /api/v1.0/images
        '''
        args = parser.parse_args()
        img = args['file']
        if not img.content_type in current_app.config['CONTENT_TYPE']:
            return {'message': 'Unauthorized type'}, 400
        db = main.db.get_db()
        checked_name = db.execute('SELECT name FROM image WHERE name=?',
                              (img.filename,)).fetchone()
        if checked_name: 
            return {'message': 'picture name already exists'}, 400
        try:
            saved_path = os.path.join(current_app.config['IMAGE_DIR'], img.filename)
            img.save(saved_path)
            date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            db.execute('INSERT INTO  image (name, date) VALUES (?, ?)',
                (img.filename, date))
            db.commit()
            current_image= db.execute('SELECT id, name FROM image WHERE name=?',
                (img.filename,)).fetchone()
            id, _ = current_image
            return {'message': 'Image added to collection',
                    'image_url': url_for('bp.aboutimage', image_id=id),
                   }

        except sqlite3.Error as error:
                return {'message': error}, 500
    

class AboutImage(Resource):
        
        def get(self, image_id):
            ''' 
            Get about image
            GET /api/v1.0/images/<int:image_id>
            '''
            db = main.db.get_db()
            image = db.execute('SELECT name, date FROM image WHERE id=?',
                              (image_id,)).fetchone()
            if image:
                name, date = image
                return {'name': name,
                        'time': date.strftime("%Y-%m-%d %H:%M:%S"),
                        'file_url': url_for('bp.itemfile', file_name=name),
                        'comm_url': url_for('bp.itemimage', image_id=image_id)
                       }
            return {'message': 'Image not found'}, 404
