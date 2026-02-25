"""Domain models for the Todo application."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum

from core.constants import MAX_TITLE_LENGTH, MAX_DESCRIPTION_LENGTH
from domain.exceptions import ValidationError


class Priority(StrEnum):
    """Task priority levels."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class TaskStatus(StrEnum):
    """Task completion status."""

    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"


@dataclass
class Task:
    """Represents a task in the Todo application.

    Attributes:
        id: Unique identifier for the task.
        title: Task title (required, max 200 chars).
        description: Optional task description (max 1000 chars).
        priority: Task priority level.
        due_date: Optional due date.
        status: Current completion status.
        created_at: Timestamp when task was created.
    """

    id: int
    title: str
    description: str | None = None
    priority: Priority = Priority.MEDIUM
    due_date: datetime | None = None
    status: TaskStatus = TaskStatus.ACTIVE
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Validate task invariants after initialization."""
        self._validate_title()
        self._validate_description()
        self._validate_priority()
        self._validate_status()

    def _validate_title(self) -> None:
        """Validate title constraints."""
        if not self.title or not self.title.strip():
            raise ValidationError("Title cannot be empty.")

        stripped = self.title.strip()
        if len(stripped) > MAX_TITLE_LENGTH:
            raise ValidationError(
                f"Title must not exceed {MAX_TITLE_LENGTH} characters."
            )

        self.title = stripped

    def _validate_description(self) -> None:
        """Validate description constraints."""
        if self.description is not None:
            if len(self.description) > MAX_DESCRIPTION_LENGTH:
                raise ValidationError(
                    f"Description must not exceed {MAX_DESCRIPTION_LENGTH} characters."
                )
            self.description = self.description.strip() or None

    def _validate_priority(self) -> None:
        """Validate priority is a valid Priority enum value."""
        if isinstance(self.priority, str):
            try:
                self.priority = Priority(self.priority.upper())
            except ValueError:
                raise ValidationError(
                    f"Priority must be one of: {', '.join(p.value for p in Priority)}."
                )
        elif not isinstance(self.priority, Priority):
            raise ValidationError(
                f"Priority must be one of: {', '.join(p.value for p in Priority)}."
            )

    def _validate_status(self) -> None:
        """Validate status is a valid TaskStatus enum value."""
        if isinstance(self.status, str):
            try:
                self.status = TaskStatus(self.status.upper())
            except ValueError:
                raise ValidationError(
                    f"Status must be one of: {', '.join(s.value for s in TaskStatus)}."
                )
        elif not isinstance(self.status, TaskStatus):
            raise ValidationError(
                f"Status must be one of: {', '.join(s.value for s in TaskStatus)}."
            )

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.status = TaskStatus.COMPLETED

    def mark_active(self) -> None:
        """Mark the task as active."""
        self.status = TaskStatus.ACTIVE

    def toggle_completion(self) -> None:
        """Toggle between active and completed status."""
        if self.status == TaskStatus.ACTIVE:
            self.mark_completed()
        else:
            self.mark_active()
