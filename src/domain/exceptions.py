"""Domain-specific exception classes for the Todo application."""


class DomainError(Exception):
    """Base class for all domain exceptions."""

    pass


class ValidationError(DomainError):
    """Raised when input validation fails."""

    pass


class TaskNotFoundError(DomainError):
    """Raised when a task with the specified ID is not found."""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found.")
