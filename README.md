Код решения тестового задания. Цель: Быстро написать REST API на фреймворке который не знает ни одна нейронка, т.е. проверка как соискатель быстро освоится с документацией и реализует функционал. На момент написания, последнюю версию LiteStar 2.16.0 нейронки не знали. Так же требовалось интегрировать несколько библиотек: alembic. Использовать новую ORM advanced-alchemy 

# REST API для управления пользователями с LiteStar и PostgreSQL
----
## Структура проекта
```text
user-management-api/
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
└── app/
    ├── __init__.py
    ├── db/
    │   ├── __init__.py
    │   ├── models.py
    │   └── session.py
    ├── domain/
    │   ├── __init__.py
    │   └── users/
    │       ├── __init__.py
    │       ├── schemas.py
    │       ├── service.py
    │       └── controllers.py
    └── main.py
```
## Шаги развертывания

### 1. Клонируйте репозиторий с GitHub:
`git clone https://github.com/yourusername/user-management-api.git`

`cd user-management-api`

### 2. Собераем и запускаем контейнеры
`docker-compose down && docker-compose up --build`

Приложение будет доступно по адресу http://localhost:8000

Swagger по адресу http://localhost:8000/schema/swagger

---

## Миграции

Используем синхронный движок только для миграций , а в самом приложении продолжить использовать асинхронный

На старте приложения, применяются миграции.

---

## Проверки

Файл `prestart.py`.
Перед запуском приложения, сделана проверка на возможность подключения к БД по переданным параметрам.

---

## API Endpoints

* POST `/users` - Создание пользователя

* GET `/users` - Получение списка пользователей

* GET `/users/{user_id}` - Получение данных одного пользователя

* PUT `/users/{user_id}` - Обновление данных пользователя

* DELETE `/users/{user_id}` - Удаление пользователя
* 
----

###Локальный запуск 

`litestar --app app.main:app run`

Если требуется "reload mode,"

`litestar --app app.main:app run --reload`

-----
