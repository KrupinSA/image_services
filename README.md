Приложение построено на функциональности CRUD.
| Действие | Метод | URL | Описание |
|----------|-------|-----|----------|
| Create | POST | /api/v1.0/images | Добавить картинку |
| Create | POST | /api/v1.0/images/*<int:image_id>*/comments | Добавить комментарий к картике по ее id |
| Read | GET | /api/v1.0/images | Вывести коллекцию картинок |
| Read | GET | /api/v1.0/images/*<int:image_id>* | Показать информацию о картинке |
| Read | GET | /api/v1.0/file/*<string:file_name>* | Скачать картинку с именем file_name |
| Read | GET | /api/v1.0/images/*<int:image_id>*/comments | Вывести коллекцию комментариев для картинки с id | 
| Update | PUT | /api/v1.0/comments/*<int:comment_id>* | Изменить комментарий по его id |
| Delete | DELETE | /api/v1.0/comments/*<int:comment_id>* | Удалить комментарий по его id |

Тестирование.
```sh
$ pytest

================================================================================ test session starts ================================================================================
platform linux -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /home/serg/devman/srvhub/work/projects/image_services
collected 10 items                                                                                                                                                                  

tests/test_comm.py ...                                                                                                                                                        [ 30%]
tests/test_db.py ..                                                                                                                                                           [ 50%]
tests/test_factory.py .                                                                                                                                                       [ 60%]
tests/test_img.py ....                                                                                                                                                        [100%]

================================================================================ 10 passed in 0.63s =================================================================================
```
Тестированием выполн
