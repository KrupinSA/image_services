Приложение построено на функциональности CRUD.
| Действие | Метод | URL | Описание |
|----------|-------|-----|----------|
| Create | POST | /api/v1.0/images | Добавить картинку |
| Create | POST | /api/v1.0/images/*<int:image_id>*/comments | Добавить комментарий к картике по ее id |
| Read | GET | /api/v1.0/images | Вывести коллекцию картинок |
| Read | GET | /api/v1.0/file/*<string:file_name>* | Скачать картинку с именем file_name |
| Read | GET | /api/v1.0/images/*<int:image_id>*/comments | Вывести коллекцию комментариев для картинки с id | 
| Update | PUT | /api/v1.0/comments/*<int:comment_id>* | Изменить комментарий по его id |
| Delete | DELETE | /api/v1.0/comments/*<int:comment_id>* | Удалить комментарий по его id |
