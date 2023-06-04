# CSV - API
    Основная информация
    HTTP сервис, предназначенный для работы с импортируемыми данными в формате csv различного формата.
    
    Реализованы возможности получения списка файлов с информацией о колонках, данных по конкретному файлу с опциолнальными фильтрацией и сортировкой по столбцам.
    Реализована авторизация пользователя, эндпоинт для удаления ранее загруженного файла, система кеширования на базе Redis, написан Dockerfile для запуска в Docker.

    **Запрос/Ответ**
    | Запрос  | Ответ |
    | ----------------- | ----------------- |
    | curl -X 'GET' \ 'http://127.0.0.1:8000/files/review' \ -H 'accept: application/json' | Response code: 200    Response body:    {"status": "success",    "data": [    {    "test3": [    "id",    "value",    "logid",    "date"    ]    },    ],    "details": null    }|
