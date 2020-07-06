from flask import jsonify 

def bad_request(e):
    response = jsonify({'message': 'bad request'})
    response.status_code = 400
    return response

def page_not_found(e):
    response = jsonify({'message': 'source not found'})
    response.status_code = 404
    return response

def internal_server_error(e):
    response = jsonify({'message': 'Internal server error'})
    response.status_code = 500
    return response