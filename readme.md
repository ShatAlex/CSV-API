# CSV - API

    1. Основная информация
    HTTP сервис, предназначенный для работы с импортируемыми данными в формате csv различного формата.
    
    Реализованы возможности получения списка файлов с информацией о колонках, данных по конкретному файлу с опциолнальными
    фильтрацией и сортировкой по столбцам. Реализована авторизация пользователя, эндпоинт для удаления ранее загруженного файла, 
    система кеширования на базе Redis, написан Dockerfile для запуска в Docker.

    2. Запрос/Ответ
![get_review](https://github.com/ShatAlex/CSV-API/blob/master/get_review.png)
    2.1 Запрос и ответ на получение списка файлов с информацией о колонках
| Запрос                | Ответ                                                                           |
|-----------------------|---------------------------------------------------------------------------------|                                                             
| curl -X 'GET' \ 'http://127.0.0.1:8000/files/review' \ <br/>-H 'accept: application/json' | Response code: 200<br/>Response body:<br/>{<br/>&nbsp;&nbsp;&nbsp;"status": "success", <br/>&nbsp;&nbsp;&nbsp;"data": [<br/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"test": [<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"logid",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"date"<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br/>&nbsp;&nbsp;&nbsp;&nbsp;],<br/>&nbsp;&nbsp;&nbsp;"details": null<br/>}|
