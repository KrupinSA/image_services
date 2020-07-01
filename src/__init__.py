import os
from flask import Flask
from flask_restful import Api

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True )
    app.config.from_mapping(
        DATABASE=os.path.join(os.path.dirname(__file__), 'resources', 'db', 'src.sqlite'),
        IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'resources', 'images')
    )

    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from .views import bp_views
    from .views.ImagesView import ItemImage, ImagesList, AboutImage
    from .views.CommentsView import ItemComments
    from .views.FilesView import ItemFile

    api = Api(bp_views)
    api.add_resource(ItemImage, '/images/<int:image_id>/comments')
    api.add_resource(AboutImage, '/images/<int:image_id>')
    api.add_resource(ImagesList, '/images')
    api.add_resource(ItemComments, '/comments/<int:comment_id>')
    api.add_resource(ItemFile, '/file/<string:file_name>')


    app.register_blueprint(bp_views)
    from .main import db
    db.init_app(app)

    return app