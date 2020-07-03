import os
from werkzeug.datastructures import FileStorage

def test_get_img_collection(client):
    '''
    Тест вывода коллекции картинок.
    Корректный запрос.
    '''
    rv = client.get('/api/v1.0/images')
    assert ['cat1.jpg', 'cat2.jpg', 'cat3.jpg'] == sorted([image['name'] for image in rv.get_json()['images']])

    '''
    Некорректный запрос.
    '''
    rv = client.get('/api/v1.0/images/')
    assert {'message': 'source not found'} == rv.get_json()


def test_get_img_info(client):
    '''
    Тест вывода информации о картинке.
    Корректный запрос.
    '''
    rv = client.get('/api/v1.0/images/1')
    assert {'name': 'cat1.jpg',
            'time': '2018-01-01 00:00:00',
            'file_url': '/api/v1.0/file/cat1.jpg',
            'comm_url': '/api/v1.0/images/1/comments'} == rv.get_json()

    '''
    Некорректный запрос.
    Нет такого id в БД.
    '''
    rv = client.get('/api/v1.0/images/4')
    assert {'message': 'Image not found'} == rv.get_json()


def test_get_img(client):
    '''
    Тест загрузить файл картинки клиенту.
    Корректный запрос.
    '''
    rv = client.get('/api/v1.0/images/1')
    file_url = rv.get_json()['file_url']
    rv = client.get(file_url)
    image = rv.get_data()
    image_path = os.path.join(os.path.dirname(__file__), 'tmp_img', 'cat4.jpg')
    with open(image_path, 'wb') as image_file:
        image_file.write(image)

    with open(image_path, 'rb') as image_file:
        loaded_image = image_file.read()

    assert loaded_image ==  image           
    '''
    Некорректный запрос.
    Нет такого файла.
    '''
    rv = client.get('/api/v1.0/file/bad_file.jpg')
    assert {'message': 'File not found'} == rv.get_json()


def test_upload_img(client):
    '''
    Тест на загрузку файла картинки на сервер.
    Корректный запрос.
    '''
    image_path = os.path.join(os.path.dirname(__file__), 'tmp_img', 'cat4.jpg')
    img_file = FileStorage(
                   stream=open(image_path, "rb"),
                   filename="cat4.jpg",
                   content_type="image/jpeg",
    )
  
    response = client.post('/api/v1.0/images',
                           content_type='multipart/form-data',
                           data={'file': img_file,
                           },
                          )    

    img_file.close()
    assert '200' in  response.status           

    '''
    Некорректный запрос.
    Такой файл уже существует.
    '''
    img_file = FileStorage(
                   stream=open(image_path, "rb"),
                   filename="cat4.jpg",
                   content_type="image/jpeg",
    )
  
    response = client.post('/api/v1.0/images',
                           content_type='multipart/form-data',
                           data={'file': img_file,
                           },
                          )    

    
    assert '400' in  response.status
