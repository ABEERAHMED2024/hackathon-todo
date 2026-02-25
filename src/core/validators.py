"""Input validation functions for the Todo application."""

from datetime import datetime

from domain.exceptions import ValidationError
from core.constants import (
    MAX_TITLE_LENGTH,
    MAX_DESCRIPTION_LENGTH,
    PRIORITY_LEVELS,
    DATE_FORMAT,
)


def validate_title(title: str) -> str:
    """Validate and return a task title.

    Args:
        title: The title string to validate.

    Returns:
        The validated title string.

    Raises:
        ValidationError: If title is empty, whitespace-only, or exceeds max length.
    """
    if not title or not title.strip():
        raise ValidationError("Title cannot be empty.")

    stripped = title.strip()
    if len(stripped) > MAX_TITLE_LENGTH:
        raise ValidationError(f"Title must not exceed {MAX_TITLE_LENGTH} characters.")

    return stripped


def validate_description(description: str | None) -> str | None:
    """Validate and return a task description.

    Args:
        description: The description string to validate, or None.

    Returns:
        The validated description string, or None if input was None/empty.

    Raises:
        ValidationError: If description exceeds max length.
    """
    if description is None or not description.strip():
        return None

    if len(description) > MAX_DESCRIPTION_LENGTH:
        raise ValidationError(
            f"Description must not exceed {MAX_DESCRIPTION_LENGTH} characters."
        )

    return description.strip()


def validate_priority(priority: str) -> str:
    """Validate and return a priority level.

    Args:
        priority: The priority string to validate.

    Returns:
        The validated priority in uppercase.

    Raises:
        ValidationError: If priority is not a valid level.
    """
    if not priority:
        raise ValidationError("Priority cannot be empty.")

    normalized = priority.strip().upper()
    if normalized not in PRIORITY_LEVELS:
        raise ValidationError(
            f"Priority must be one of: {', '.join(PRIORITY_LEVELS)}."
        )

    return normalized


def validate_date(date_str: str | None) -> datetime | None:
    """Validate and return a date object.

    Args:
        date_str: The date string in YYYY-MM-DD format, or None.

    Returns:
        A datetime object, or None if input was None/empty.

    Raises:
        ValidationError: If date format is invalid or date is not valid.
    """
    if not date_str or not date_str.strip():
        return None

    stripped = date_str.strip()
    try:
        return datetime.strptime(stripped, DATE_FORMAT)
    except ValueError:
        raise ValidationError(
            f"Date must be in {DATE_FORMAT} format (e.g., 2026-02-24)."
        )


def validate_task_id(task_id: int) -> int:
    """Validate and return a task ID.

    Args:
        task_id: The task ID to validate.

    Returns:
        The validated task ID.

    Raises:
        ValidationError: If task_id is not a positive integer.
    """
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValidationError("Task ID must be a positive integer.")

    return task_id
