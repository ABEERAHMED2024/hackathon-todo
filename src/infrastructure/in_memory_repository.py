"""In-memory implementation of the task repository."""

from domain.exceptions import TaskNotFoundError
from domain.models import Task
from domain.repositories import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of TaskRepository.

    Stores tasks in a private dictionary keyed by task ID.
    This implementation is suitable for Phase I (console MVP) where
    no persistence is required.

    Attributes:
        _tasks: Private dictionary mapping task IDs to Task instances.
    """

    def __init__(self) -> None:
        """Initialize an empty in-memory repository."""
        self._tasks: dict[int, Task] = {}

    def add(self, task: Task) -> None:
        """Add a new task to storage.

        Args:
            task: The task to add.
        """
        self._tasks[task.id] = task

    def get_all(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            A list of all tasks in the repository.
        """
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Task | None:
        """Retrieve a task by ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The task if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def update(self, task: Task) -> None:
        """Update an existing task.

        Args:
            task: The task with updated values.

        Raises:
            TaskNotFoundError: If the task does not exist.
        """
        if task.id not in self._tasks:
            raise TaskNotFoundError(task.id)
        self._tasks[task.id] = task

    def delete(self, task_id: int) -> None:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete.

        Raises:
            TaskNotFoundError: If the task does not exist.
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        del self._tasks[task_id]
