"""Repository abstraction for task data access."""

from abc import ABC, abstractmethod

from domain.models import Task


class TaskRepository(ABC):
    """Abstract base class defining the task repository interface.

    This class defines the contract that any task repository implementation
    must follow. It enables dependency injection and swapping of storage
    backends without modifying business logic.
    """

    @abstractmethod
    def add(self, task: Task) -> None:
        """Add a new task to storage.

        Args:
            task: The task to add.
        """
        pass

    @abstractmethod
    def get_all(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            A list of all tasks.
        """
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task | None:
        """Retrieve a task by ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            The task if found, None otherwise.
        """
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        """Update an existing task.

        Args:
            task: The task with updated values.

        Raises:
            TaskNotFoundError: If the task does not exist.
        """
        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete.

        Raises:
            TaskNotFoundError: If the task does not exist.
        """
        pass
