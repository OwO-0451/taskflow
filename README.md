# TaskFlow — REST API менеджер задач

**TaskFlow** — это учебный REST API сервер для управления задачами, проектами и пользователями. Проект разработан в рамках курса «Информационные технологии в профессиональной деятельности» и демонстрирует полный цикл проектирования: от составления технического задания и проектирования схемы БД до реализации бэкенда.

[![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Описание
Приложение позволяет пользователям регистрироваться, создавать проекты, управлять задачами (создавать, назначать исполнителей, менять статусы и приоритеты) и оставлять комментарии. Архитектура построена по принципам REST, где каждая сущность (пользователь, проект, задача, комментарий) представлена в виде ресурса с собственным набором эндпоинтов.

## Стек
*   **Язык:** Python 3.9+
*   **Фреймворк:** Flask
*   **ORM:** SQLAlchemy
*   **База данных:** SQLite
*   **Валидация:** Marshmallow (или Pydantic)
*   **Аутентификация:** JWT (JSON Web Tokens)

## Инструкция по установке

1.  **Клонирование репозитория:**
    ```bash
    git clone <ссылка_на_репозиторий>
    cd taskflow
    ```
2.  **Создание и активация виртуального окружения:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```
3.  **Установка зависимостей:**
    ```bash
    pip install -r requirements.txt
    ```
    *Минимальный состав `requirements.txt`:*
    ```text
    Flask==3.0.3
    Flask-SQLAlchemy==3.1.1
    Flask-JWT-Extended==4.6.3
    marshmallow==3.21.2
    ```
4.  **Инициализация базы данных:**
    В корне проекта находится файл `schema.sql` (результат Лабораторной работы № 2). Для создания таблиц выполните:
    ```bash
    # Создаем базу, если её нет
    sqlite3 instance/taskflow.db < schema.sql
    ```
    
5.  **Запуск приложения:**
    ```bash
    python app.py
    ```
    Сервер запустится по адресу `http://127.0.0.1:5000`.

## Документация API
Подробное описание всех доступных эндпоинтов, форматов запросов и ответов, а также примеры использования (включая регистрацию, авторизацию и работу с вложенными ресурсами) приведено в отдельном файле:
*   **[API.md](API.md)**

*(Краткая справка: реализованы CRUD-операции для `/users`, `/projects`, `/tasks` и `/comments`. Для доступа к защищенным эндпоинтам требуется заголовок `Authorization: Bearer <token>`).*

## Структура проекта

```
taskflow/
├── app.py                  # Точка входа, инициализация Flask и запуск сервера
├── config.py               # Конфигурация приложения (секретные ключи, настройки БД)
├── requirements.txt        # Зависимости Python
├── schema.sql              # SQL-скрипт создания БД
├── instance/               # Папка для файла SQLite (instance/taskflow.db)
├── models/                 # Модели SQLAlchemy (User, Project, Task, Comment)
│   ├── __init__.py
│   └── user.py
│   └── project.py
│   └── task.py
│   └── comment.py
├── schemas/                # Схемы Marshmallow для сериализации/десериализации
│   ├── __init__.py
│   └── user_schema.py
│   └── project_schema.py
│   └── task_schema.py
├── routes/                 # Вьюхи (Blueprints) и обработчики API
│   ├── __init__.py
│   └── auth.py             # /auth/register, /auth/login
│   └── users.py
│   └── projects.py
│   └── tasks.py
│   └── comments.py
├── tests/                  # Модульные и интеграционные тесты
│   └── test_tasks.py
├── API.md                  # Полная документация REST API
├── README.md               # Этот файл
└── LICENSE                 # Лицензия MIT
```

## Лицензия
Данный проект распространяется под лицензией **MIT**. С подробными условиями вы можете ознакомиться в файле `LICENSE`.