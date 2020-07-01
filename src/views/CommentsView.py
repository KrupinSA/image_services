from flask_restful import Resource, url_for, reqparse
import sqlite3
from .. import main

parser = reqparse.RequestParser()
parser.add_argument('text')

class ItemComments(Resource):

    def put(self, comment_id):
        '''
        Change comment with id
        PUT /api/v1.0/comments/<int:comment_id>
        '''
        args = parser.parse_args()

        if not args['text']: return {'message': 'Empty comment'}, 400 

        db = main.db.get_db()
        checked_id = db.execute('SELECT id FROM comment WHERE id=?', (comment_id,)).fetchall()
        if checked_id:
            try:
                db.execute('UPDATE comment SET text=? WHERE id=?',
                            (args['text'], comment_id,))
                db.commit()
                return {'message':'Comment change'}, 200
            except sqlite3.Error as error:
                return {'message': error}, 500
        return {'message': 'Comment not found'}, 404



    def delete(self, comment_id):
        '''
        Delete comment with id
        DELETE /api/v1.0/comments/<int:comment_id>
        '''
        db = main.db.get_db()
        checked_id = db.execute('SELECT id FROM comment WHERE id=?', (comment_id,)).fetchall()
        if checked_id:
            try:
                db.execute('DELETE FROM  comment WHERE id=?',
                            (comment_id,))
                db.commit()
                return {'message':'Comment delete'}, 200
            except sqlite3.Error as error:
                return {'message': error}, 500
        return {'message': 'Comment not found'}, 404