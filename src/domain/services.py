"""Business logic services for the Todo application."""

from datetime import datetime

from domain.exceptions import TaskNotFoundError, ValidationError
from domain.models import Priority, Task, TaskStatus
from domain.repositories import TaskRepository


class TaskService:
    """Service class implementing business logic for task operations.

    This class orchestrates task operations by delegating data access
    to a repository implementation. It enforces business rules and
    handles domain exceptions.

    Attributes:
        repository: The task repository for data access.
    """

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize the service with a repository.

        Args:
            repository: A TaskRepository implementation for data access.
        """
        self._repository = repository

    def create_task(
        self,
        title: str,
        description: str | None = None,
        priority: str = "MEDIUM",
        due_date: datetime | None = None,
    ) -> Task:
        """Create a new task.

        Args:
            title: The task title (required).
            description: Optional task description.
            priority: Task priority (default: MEDIUM).
            due_date: Optional due date.

        Returns:
            The created task.

        Raises:
            ValidationError: If input validation fails.
        """
        if not title or not title.strip():
            raise ValidationError("Title cannot be empty.")

        next_id = self._generate_next_id()

        task = Task(
            id=next_id,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            status=TaskStatus.ACTIVE,
            created_at=datetime.now(),
        )

        self._repository.add(task)
        return task

    def get_all_tasks(
        self,
        status: TaskStatus | None = None,
        priority: Priority | None = None,
    ) -> list[Task]:
        """Retrieve all tasks with optional filtering.

        Args:
            status: Filter by task status (optional).
            priority: Filter by priority (optional).

        Returns:
            A list of tasks matching the filters, sorted by priority
            (HIGH > MEDIUM > LOW) then by creation time (oldest first).
        """
        tasks = self._repository.get_all()

        if status is not None:
            tasks = [t for t in tasks if t.status == status]

        if priority is not None:
            tasks = [t for t in tasks if t.priority == priority]

        return self._sort_tasks(tasks)

    def get_task_by_id(self, task_id: int) -> Task:
        """Retrieve a single task by ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The task with the specified ID.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        task = self._repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)
        return task

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None,
        priority: str | None = None,
        due_date: datetime | None = None,
    ) -> Task:
        """Update an existing task.

        Args:
            task_id: The ID of the task to update.
            title: New title (optional, None means no change).
            description: New description (optional).
            priority: New priority (optional).
            due_date: New due date (optional).

        Returns:
            The updated task.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
            ValidationError: If input validation fails.
        """
        task = self.get_task_by_id(task_id)

        if title is not None:
            if not title.strip():
                raise ValidationError("Title cannot be empty.")
            task.title = title

        if description is not None:
            task.description = description.strip() if description.strip() else None

        if priority is not None:
            task.priority = priority

        if due_date is not None:
            task.due_date = due_date

        self._repository.update(task)
        return task

    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        self.get_task_by_id(task_id)
        self._repository.delete(task_id)

    def toggle_completion(self, task_id: int) -> Task:
        """Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle.

        Returns:
            The task with updated status.

        Raises:
            TaskNotFoundError: If no task exists with the given ID.
        """
        task = self.get_task_by_id(task_id)
        task.toggle_completion()
        self._repository.update(task)
        return task

    def _generate_next_id(self) -> int:
        """Generate the next available task ID.

        Returns:
            A unique positive integer ID.
        """
        existing_tasks = self._repository.get_all()
        if not existing_tasks:
            return 1
        return max(t.id for t in existing_tasks) + 1

    def _sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by priority (HIGH > MEDIUM > LOW) then by creation time.

        Args:
            tasks: The list of tasks to sort.

        Returns:
            A new sorted list of tasks.
        """
        priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}
        return sorted(tasks, key=lambda t: (priority_order[t.priority], t.created_at))
