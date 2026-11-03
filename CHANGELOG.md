# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-27

### Added
- **Authentication & Authorization:** Полноценная система регистрации и входа на базе JWT.
  - Эндпоинты: `POST /api/v1/auth/register`, `POST /api/v1/auth/login`.
  - Защита маршрутов через декораторы (проверка роли `admin` и владельца ресурса).
- **Docker Support:** Контейнеризация приложения.
  - Добавлен `Dockerfile` для сборки образа.
  - Добавлен `docker-compose.yml` для оркестрации сервиса приложения и базы данных.
- **Production Deployment:** Скрипты и конфигурация для развертывания.
  - Использование переменных окружения (`.env`) для секретов (JWT_SECRET_KEY).
  - Настройка Gunicorn как production WSGI-сервера.
- **Admin Panel (API):** Расширенные права для роли администратора.
  - Эндпоинты управления пользователями: `GET /api/v1/users`, `DELETE /api/v1/users/{id}`.
- **Comments Resource:** Полная реализация CRUD для комментариев к задачам.
  - Эндпоинты: `POST /api/v1/tasks/{id}/comments`, `GET /api/v1/comments/{id}`, `PUT`, `DELETE`.

### Changed
- **Database Schema:** Обновлена структура БД с учетом миграций (добавлены индексы для полей `status`, `priority`, `deadline`).
- **API Versioning:** Все эндпоинты переведены на префикс `/api/v1/`.
- **Security:** Пароли теперь хешируются алгоритмом Bcrypt перед сохранением в SQLite.

### Fixed
- Исправлена логика каскадного удаления: при удалении пользователя-владельца проекты теперь переходят к администратору вместо удаления (изменено `ON DELETE RESTRICT` на каскадное обновление связей).

## [0.2.0] - 2026-10-15

### Added
- **Tasks CRUD:** Реализованы базовые операции для управления задачами.
  - Эндпоинты: `GET /api/v1/tasks`, `POST /api/v1/tasks`, `GET /api/v1/tasks/{id}`, `PUT /api/v1/tasks/{id}`, `DELETE /api/v1/tasks/{id}`.
- **Projects CRUD:** Реализованы базовые операции для управления проектами.
  - Эндпоинты: `GET /api/v1/projects`, `POST /api/v1/projects`, `GET /api/v1/projects/{id}`, `PUT /api/v1/projects/{id}`, `DELETE /api/v1/projects/{id}`.
- **Filtering & Pagination:** Поддержка фильтрации задач по `project_id`, `status`, `priority` и пагинации через query-параметры (`limit`, `offset`).
- **Database Schema:** Внедрена реляционная схема (файл `schema.sql` / `alembic` миграции).
  - Таблицы: `users`, `projects`, `tasks`, `comments`.
  - Связи: `ON DELETE CASCADE` для задач и комментариев, `ON DELETE RESTRICT` для владельцев проектов.

### Changed
- **Project Structure:** Структура папок приведена к модульному виду (`models/`, `routes/`, `schemas/`).
- **Validation:** Добавлена валидация входящих данных через Marshmallow (или Pydantic) схемы.

## [0.1.0] - 2026-09-29

### Added
- **Project Scaffolding:** Инициализация учебного Flask-проекта.
- **Core Dependencies:** Настройка `requirements.txt` (Flask, Flask-SQLAlchemy, Marshmallow).
- **Database Stub:** Файл `schema.sql` с пустыми заготовками таблиц.
- **Basic Configuration:** Файл `config.py` для загрузки переменных окружения.
- **Entry Point:** Файл `app.py` с базовой инициализацией Flask приложения.