import sqlite3
from datetime import datetime
from typing import List, Optional

from src.domain.models import Task, Priority, TaskStatus
from src.domain.repositories import TaskRepository
from src.infrastructure.database import get_connection


class SQLiteTaskRepository(TaskRepository):

    def __init__(self) -> None:
        from src.infrastructure.database import init_database
        init_database()

    def _row_to_task(self, row: sqlite3.Row) -> Task:
        return Task(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            priority=Priority(row["priority"]),
            due_date=datetime.fromisoformat(row["due_date"]) if row["due_date"] else None,
            status=TaskStatus(row["status"]),
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def _task_to_dict(self, task: Task) -> dict:
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority.value,
            "status": task.status.value,
            "due_date": task.due_date.isoformat() if task.due_date else None,
            "created_at": task.created_at.isoformat(),
        }

    def add(self, task: Task) -> Task:
        data = self._task_to_dict(task)
        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO tasks (title, description, priority, status, due_date, created_at)
                VALUES (:title, :description, :priority, :status, :due_date, :created_at)
                """,
                data,
            )
            conn.commit()
            task.id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        return task

    def get_all(self) -> List[Task]:
        with get_connection() as conn:
            cursor = conn.execute("SELECT * FROM tasks ORDER BY created_at ASC")
            rows = cursor.fetchall()
            return [self._row_to_task(row) for row in rows]

    def get_by_id(self, task_id: int) -> Optional[Task]:
        with get_connection() as conn:
            cursor = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return self._row_to_task(row)

    def update(self, task: Task) -> None:
        data = self._task_to_dict(task)
        with get_connection() as conn:
            conn.execute(
                """
                UPDATE tasks
                SET title = :title,
                    description = :description,
                    priority = :priority,
                    status = :status,
                    due_date = :due_date,
                    created_at = :created_at
                WHERE id = :id
                """,
                data,
            )
            conn.commit()

    def delete(self, task_id: int) -> None:
        with get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()