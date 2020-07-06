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

Иформация о картинках(имя, дата создания) и коментарии хранятся с БД.
Сами файлы по умолчанию лежат в директории instance/resources/images.

Этапы работы с сервером.

Инициализация БД. 
```sh
$ export FLASK_APP=img_app
$ flask init-db
```

Запуск сервера.
```sh
$ export FLASK_APP=img_app
$ export FLASK_ENV=development
$ flask run
```

В БД можно записать картинки из временной директории instance/resources/tmp_img/
```sh
$ export FLASK_APP=img_app
$ flask image-to-db
```
Либо указать путь
```sh
$ export FLASK_APP=img_app
$ flask image-to-db -p /home/user/images/
```

Тестирование.
```sh
$ python -m pytest

======================================== test session starts ========================================
platform linux -- Python 3.8.2, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /home/serg/devman/srvhub/projects/image_services/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/serg/devman/srvhub/work/projects/image_services
collected 12 items                                                                                  

tests/test_comm.py::test_get_collection_comments PASSED                                       [  8%]
tests/test_comm.py::test_add_new_commen PASSED                                                [ 16%]
tests/test_comm.py::test_delete_comment PASSED                                                [ 25%]
tests/test_comm.py::test_change_commen PASSED                                                 [ 33%]
tests/test_db.py::test_get_close_db PASSED                                                    [ 41%]
tests/test_db.py::test_init_db_command PASSED                                                 [ 50%]
tests/test_db.py::test_image_to_db_command PASSED                                             [ 58%]
tests/test_factory.py::test_config PASSED                                                     [ 66%]
tests/test_img.py::test_get_img_collection PASSED                                             [ 75%]
tests/test_img.py::test_get_img_info PASSED                                                   [ 83%]
tests/test_img.py::test_download_img PASSED                                                   [ 91%]
tests/test_img.py::test_upload_img PASSED                                                     [100%]
```
Тестированием выполняются следующие проверки:
1. Передача конфигурации в фабричную функцию.
2. Инициализация БД с командной строки (flask init-db, flask image-to-db)
3. Вывод коллекции картинок. Два запроса, корректный/некорректный.
4. Вывод информации о картинке. Два запроса, id картинки существует/несуществует. Url о картинке отдается в ответе при добавлении картинки.
5. Загрузка файла в сторону клиента. Два запроса, при корректном в директории /test/tmp_img/ появляется файл cat4.jpg. Ссылка для скачивания файла берется из url_file информации о картинке. Некорректный запрос - нет такого файла.
6. Выгрузка файла на сервер. При корректном запросе сервер возвращает статус 200 (файл скопирован в директорию сервера и в БД создана соответствующая запись).
При существовании такого же имени файла в БД возращается ошибка 400 - файл не сохраняется.
7. Вывод коллекции комментариев для картинки id 1 - корректный запрос. Некорректный запрос - запрос коллекции комментариев с несуществующим id картинки.
8. Добавить новый комментарий к картинке с id 1 -корректный. Некорректный -добавить комментарий к несуществующей картинке.
9. Удалить комментарий с id 
