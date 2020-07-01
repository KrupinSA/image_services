from . import bp_views
from flask import jsonify

@bp_views.app_errorhandler(404)
def page_not_found(e):
    response = jsonify({'message': 'source not found'})
    response.status_code = 404
    return response

@bp_views.app_errorhandler(500)
def internal_server_error(e):
    response = jsonify({'message': 'Internal server error'})
    response.status_code = 500
    return response