def test_get_collection_comments(client):
    '''
    Тест вывода коллекции коментариев для картинки с id 1.
    Корректный запрос.
    '''
    rv = client.get('/api/v1.0/images/1/comments')
    assert {'comments': [{'comm': 'комментарий1', 'comm_url': '/api/v1.0/comments/1'},
                         {'comm': 'комментарий2', 'comm_url': '/api/v1.0/comments/2'}],
                         'img_url': '/api/v1.0/images/1'} == rv.get_json()

    '''
    Некорректный запрос.
    Нет картинки с таким id в БД.
    '''
    rv = client.get('/api/v1.0/images/4/comments')
    assert {'message': 'Image not found'} == rv.get_json()


def test_add_new_commen(client):
    '''
    Тест на добавление нового комментария к картинке с id 1.
    Корректный запрос.
    '''
   
    response = client.post('/api/v1.0/images/1/comments',
                           data={'text':'Comment4'})    

    assert '201' in  response.status           

    ''',
    Некорректный запрос.
    Файла с таким id не существует.
    '''
    
    response = client.post('/api/v1.0/images/9/comments',
                           data={'text':'Comment5'})    

    assert '404' in  response.status 
    
def test_delete_comment(client):
    '''
    Тест на удаление комментария  с id 1.
    Корректный запрос.
    '''
   
    response = client.delete('/api/v1.0/comments/1')    
    assert '200' in  response.status           

    '''
    Некорректный запрос.
    Комментария с таким id не существует.
    '''
    
    response = client.delete('/api/v1.0/comments/1')    
    assert '404' in  response.status 
    


def test_change_commen(client):
    '''
    Тест на изменение комментария с id 1.
    Корректный запрос.
    '''
   
    response = client.put('/api/v1.0/comments/1',
                           data={'text':'CommentChange'})    

    assert {'message': 'Comment change'} ==  response.get_json()         

    '''
    Некорректный запрос.
    Комментария с таким id не существует.
    '''
    
    response = client.put('/api/v1.0/comments/9',
                           data={'text':'Comment5'})    

    assert '404' in  response.status 