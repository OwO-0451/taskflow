PRAGMA foreign_keys = ON;

-- Таблица users
CREATE TABLE users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT    NOT NULL,
    email         TEXT    NOT NULL UNIQUE,
    password_hash TEXT    NOT NULL,
    created_at    TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- Таблица projects
CREATE TABLE projects (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    description TEXT,
    owner_id    INTEGER NOT NULL,
    created_at  TEXT    NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (owner_id)
        REFERENCES users (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- Таблица tasks
CREATE TABLE tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    description TEXT,
    status      TEXT    NOT NULL DEFAULT 'todo'
                        CHECK (status IN ('todo', 'in_progress', 'done', 'cancelled')),
    priority    TEXT    NOT NULL DEFAULT 'medium'
                        CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
    project_id  INTEGER NOT NULL,
    assignee_id INTEGER,
    created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
    deadline    TEXT,

    FOREIGN KEY (project_id)
        REFERENCES projects (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (assignee_id)
        REFERENCES users (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Таблица comments
CREATE TABLE comments (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id    INTEGER NOT NULL,
    author_id  INTEGER NOT NULL,
    text       TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (task_id)
        REFERENCES
