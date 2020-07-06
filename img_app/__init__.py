import os
from flask import Flask, Blueprint,jsonify
from flask_restful import Api


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True )

    try:
        os.makedirs(os.path.join(app.instance_path, 'resources', 'images'))
        os.makedirs(os.path.join(app.instance_path, 'resources', 'db'))
        os.makedirs(os.path.join(app.instance_path, 'resources', 'tmp_img'))

    except OSError:
        pass

    app.config.from_mapping(
        DATABASE = os.path.join(app.instance_path, 'resources', 'db', 'src.sqlite'),
        IMAGE_DIR = os.path.join(app.instance_path, 'resources', 'images'),
        CONTENT_TYPE = ['image/jpeg',],
        TMP_IMG = os.path.join(app.instance_path, 'resources', 'tmp_img'),
    )

    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    

    bp_views = Blueprint('bp', __name__, url_prefix='/api/v1.0')
    
    from .views.views import ItemImage, ImagesList, AboutImage, ItemComments, ItemFile 
    from .views import errors
    
    api = Api(bp_views)

    api.add_resource(ItemImage, '/images/<int:image_id>/comments', endpoint='comments')
    api.add_resource(AboutImage, '/images/<int:image_id>')
    api.add_resource(ImagesList, '/images', endpoint='images')
    api.add_resource(ItemComments, '/comments/<int:comment_id>')
    api.add_resource(ItemFile, '/file/<string:file_name>')
    

    app.register_blueprint(bp_views)
    app.register_error_handler(400, errors.bad_request)
    app.register_error_handler(404, errors.page_not_found)
    app.register_error_handler(500, errors.internal_server_error)

    from .main import db
    db.init_app(app)


    return app