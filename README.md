Приложение построено на функциональности CRUD.
| Действие | Метод | URL | Описание |
|----------|-------|-----|----------|
| Create | POST | /api/v1.0/images | Добавить картинку |
| Create | POST | /api/v1.0/images/image_id/comments | Добавить комментарий к картике по ее id |
| Read | GET | /api/v1.0/images | Вывести коллекцию картинок |
| Read | GET | /api/v1.0/images/image_id/comments | Вывести коллекцию комментариев для картинки с id | 
| Update | PUT | /api/v1.0/images/images_id/comments/comments_id | Изменить комментарий по его id |
| Delete | DELETE | /api/v1.0/images/images_id/comments/comments_id | Удалить комментарий по его id |
