def get_tasks(db_session, status_filter=None, limit=10, offset=0):
    """
    # Получает список задач из базы данных с возможностью фильтрации по статусу и пагинацией.

    Данная функция выполняет SQL-запрос к таблице задач. Если передан параметр status_filter,
    функция вернет только задачи с соответствующим статусом. Параметры limit и offset 
    используются для реализации пагинации (разбиения на страницы), чтобы не перегружать 
    клиента большим объемом данных за один раз.

    Args:
        db_session: Активная сессия SQLAlchemy для взаимодействия с базой данных.
        status_filter (str, optional): Строка для фильтрации задач по статусу 
            (например, 'todo', 'in_progress', 'done'). Если None, фильтрация не применяется.
        limit (int, optional): Максимальное количество задач, возвращаемых за один запрос. 
            По умолчанию равно 10.
        offset (int, optional): Количество задач, которые нужно пропустить от начала списка. 
            Используется для перехода на следующие страницы. По умолчанию равно 0.

    Returns:
        list: Список объектов Task, преобразованных в словари для удобства сериализации 
        в JSON-формат. Каждый словарь содержит ключи: id, title, description, status, priority.
    """
    # Начинаем формировать запрос к таблице задач через SQLAlchemy ORM
    query = db_session.query(Task)

    # Если передан фильтр по статусу, добавляем условие WHERE status = :status_filter
    if status_filter:
        query = query.filter(Task.status == status_filter)

    # Применяем ограничение на количество строк (LIMIT) и смещение (OFFSET)
    # Это стандартная практика для реализации пагинации в API
    query = query.limit(limit).offset(offset)

    # Выполняем запрос и получаем список объектов Task из базы данных
    tasks_from_db = query.all()

    # Преобразуем объекты SQLAlchemy в простые словари (сериализация)
    # Это необходимо, чтобы Flask мог корректно преобразовать данные в JSON
    tasks_list = []
    for task in tasks_from_db:
        task_dict = {
            'id': task.id,                      # Уникальный идентификатор задачи
            'title': task.title,                # Заголовок задачи
            'description': task.description,    # Описание задачи (может быть None)
            'status': task.status,              # Текущий статус задачи
            'priority': task.priority           # Приоритет задачи
        }
        tasks_list.append(task_dict)

    # Возвращаем готовый список словарей
    return tasks_list