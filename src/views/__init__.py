from flask import Blueprint

bp_views = Blueprint('bp', __name__, url_prefix='/api/v1.0')


from . import ImagesView, CommentsView, FilesView, errors