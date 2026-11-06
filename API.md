# API Documentation: TaskFlow

**Base URL:** `http://127.0.0.1:5000/api/v1`
**Content-Type:** `application/json`
**Authentication:** Большинство эндпоинтов требуют передачи JWT-токена в заголовке: `Authorization: Bearer <access_token>`

Authentication
Register a new user

Создает нового пользователя в системе.

**Method:** `POST`
**Path:** `/auth/register`
**Access:** Anonymous
**Request Body:**
```json
{
  "username": "maxim_dev",
  "email": "maxim@example.com",
  "password": "StrongP@ssw0rd!"
}
```
**Success Response (201 Created):**
```json
{
  "id": 1,
  "username": "maxim_dev",
  "email": "maxim@example.com"
}
```
Get access token

Авторизует пользователя и возвращает JWT-токен.

**Method:** `POST`
**Path:** `/auth/login`
**Access:** Anonymous
**Request Body:**
```json
{
  "email": "maxim@example.com",
  "password": "StrongP@ssw0rd!"
}
```
**Success Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xYz123",
  "token_type": "bearer"
}
```
Projects
Create a project

Создает новый проект.

**Method:** `POST`
**Path:** `/projects`
**Access:** Authorized (user, admin)
**Request Body:**
```json
{
  "title": "Разработка мобильного приложения",
  "description": "Создание MVP для iOS и Android платформ"
}
```
**Success Response (201 Created):**
```json
{
  "id": 1,
  "title": "Разработка мобильного приложения",
  "owner_id": 1
}
```
Get all projects

Возвращает список проектов пользователя.

**Method:** `GET`
**Path:** `/projects`
**Access:** Authorized
**Query Parameters:** `limit` (int), `offset` (int)
**Success Response (200 OK):**
```json
[
  {
"id": 1,
"title": "Разработка мобильного приложения"

  },
  {
"id": 2,
"title": "Миграция базы данных"

  }
]
```
Get project by ID

Возвращает данные конкретного проекта.

**Method:** `GET`
**Path:** `/projects/{p_id}`
**Access:** Authorized (owner, admin)
**Success Response (200 OK):**
```json
{
  "id": 1,
  "title": "Разработка мобильного приложения",
  "description": "Создание MVP для iOS и Android платформ",
  "owner_id": 1
}
```
Update a project

Обновляет данные проекта.

**Method:** `PUT`
**Path:** `/projects/{p_id}`
**Access:** Owner, admin
**Request Body (fields are optional):**
```json
{
  "title": "Разработка мобильного приложения (v2)",
  "description": "Обновленное описание проекта"
}
```
**Success Response (200 OK):**
```json
{
  "id": 1,
  "title": "Разработка мобильного приложения (v2)",
  "description": "Обновленное описание проекта"
}
```
Delete a project

Удаляет проект (каскадно удаляет задачи и комментарии).

**Method:** `DELETE`
**Path:** `/projects/{p_id}`
**Access:** Owner, admin
**Success Response (204 No Content):** Пустой ответ.
Tasks
Create a task in a project

Создает задачу внутри указанного проекта.

**Method:** `POST`
**Path:** `/projects/{p_id}/tasks`
**Access:** Owner, admin
**Request Body:**
```json
{
  "title": "Написать документацию API",
  "description": "Сформировать OpenAPI спецификацию",
  "priority": "high",
  "executor_id": 1
}
```
**Success Response (201 Created):**
```json
{
  "id": 1,
  "project_id": 1,
  "status": "backlog"
}
```
Get tasks of a project

Возвращает список задач конкретного проекта.

**Method:** `GET`
**Path:** `/projects/{p_id}/tasks`
**Access:** Authorized (project member, admin)
**Query Parameters:** `limit` (int), `offset` (int), `status` (str), `priority` (str)
**Success Response (200 OK):**
```json
[
  {
"id": 1,
"title": "Написать документацию API",
"status": "backlog"

  }
]
```
Get all tasks (global)

Глобальный список задач с возможностью фильтрации.

**Method:** `GET`
**Path:** `/tasks`
**Access:** Authorized
**Query Parameters:** `project_id` (int), `executor_id` (int), `status` (str), `priority` (str), `limit` (int), `offset` (int)
**Success Response (200 OK):**
```json
[
  {
"id": 1,
"title": "Написать документацию API",
"status": "backlog"

  }
]
```
Get task by ID

Возвращает данные конкретной задачи.

**Method:** `GET`
**Path:** `/tasks/{id}`
**Access:** Owner, executor, admin
**Success Response (200 OK):**
```json
{
  "id": 1,
  "title": "Написать документацию API",
  "status": "backlog",
  "executor_id": 1
}
```
Update a task

Полное обновление задачи.

**Method:** `PUT`
**Path:** `/tasks/{id}`
**Access:** Owner, executor, admin
**Request Body (fields are optional):**
```json
{
  "title": "Написать документацию API (v2)",
  "priority": "urgent",
  "deadline": "2026-10-31T23:59:59Z"
}
```
**Success Response (200 OK):**
```json
{
  "id": 1,
  "title": "Написать документацию API (v2)",
  "status": "backlog",
  "executor_id": 1
}
```
Update task status

Частичное обновление (только смена статуса).

**Method:** `PATCH`
**Path:** `/tasks/{id}/status`
**Access:** Owner, executor, admin
**Request Body:**
```json
{
  "status": "in_progress"
}
```
**Success Response (200 OK):**
```json
{
  "id": 1,
  "status": "in_progress"
}
```
Delete a task

Удаляет задачу (каскадно удаляет комментарии).

**Method:** `DELETE`
**Path:** `/tasks/{id}`
**Access:** Owner, admin
**Success Response (204 No Content):** Пустой ответ.
Comments
Add a comment to a task

Добавляет комментарий к задаче.

**Method:** `POST`
**Path:** `/tasks/{t_id}/comments`
**Access:** Owner, executor, admin
**Request Body:**
```json
{
  "text": "Первую версию спецификации прикрепил в репозиторий."
}
```
**Success Response (201 Created):**
```json
{
  "id": 1,
  "task_id": 1,
  "text": "Первую версию спецификации прикрепил в репозиторий."
}
```
Get comments of a task

Возвращает список комментариев к задаче.

**Method:** `GET`
**Path:** `/tasks/{t_id}/comments`
**Access:** Project member, admin
**Query Parameters:** `limit` (int), `offset` (int)
**Success Response (200 OK):**
```json
[
  {
"id": 1,
"task_id": 1,
"text": "Первую версию спецификации прикрепил в репозиторий."

  }
]
```
Get comment by ID

Возвращает конкретный комментарий.

**Method:** `GET`
**Path:** `/comments/{id}`
**Access:** Project member, admin
**Success Response (200 OK):**
```json
{
  "id": 1,
  "task_id": 1,
  "text": "Первую версию спецификации прикрепил в репозиторий."
}
```
Update a comment

Редактирует текст комментария.

**Method:** `PUT`
**Path:** `/comments/{id}`
**Access:** Author, owner, admin
**Request Body:**
```json
{
  "text": "Первая версия спецификации и схема БД прикреплены в репозиторий."
}
```
**Success Response (200 OK):**
```json
{
  "id": 1,
  "task_id": 1,
  "text": "Первая версия спецификации и схема БД прикреплены в репозиторий."
}
```

# Status Codes Reference
- `200 OK` — Успешный запрос (GET, PUT).
- `201 Created` — Ресурс успешно создан (POST).
- `204 No Content` — Успешное удаление, тело ответа пустое.
- `400 Bad Request` — Ошибка валидации входных данных.
- `401 Unauthorized` — Отсутствует или недействителен токен.
- `403 Forbidden` — Доступ запрещен (недостаточно прав).
- `404 Not Found` — Ресурс не найден.
- `409 Conflict` — Конфликт (например, email уже занят).
