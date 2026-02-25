"""User input handling functions for the CLI application."""

from datetime import datetime

from core.constants import DATE_FORMAT


def prompt_title() -> str:
    """Prompt the user to enter a task title.

    Returns:
        The entered title string (stripped of whitespace).
    """
    return input("Enter title: ").strip()


def prompt_description() -> str | None:
    """Prompt the user to enter an optional task description.

    Returns:
        The entered description string, or None if skipped.
    """
    user_input = input("Enter description (or press Enter to skip): ").strip()
    return user_input if user_input else None


def prompt_priority() -> str:
    """Prompt the user to enter a task priority.

    Returns:
        The entered priority string (stripped of whitespace).
    """
    return input("Select priority (Low/Medium/High): ").strip()


def prompt_due_date() -> datetime | None:
    """Prompt the user to enter an optional due date.

    Returns:
        A datetime object if a valid date was entered, None if skipped.
    """
    user_input = input("Enter due date (YYYY-MM-DD, or press Enter to skip): ").strip()
    if not user_input:
        return None
    try:
        return datetime.strptime(user_input, DATE_FORMAT)
    except ValueError:
        raise ValueError(f"Invalid date format. Use {DATE_FORMAT} (e.g., 2026-02-24).")


def prompt_task_id() -> int:
    """Prompt the user to enter a task ID.

    Returns:
        The entered task ID as an integer.

    Raises:
        ValueError: If the input is not a valid integer.
    """
    user_input = input("Enter task ID: ").strip()
    return int(user_input)


def prompt_confirmation(message: str = "Are you sure?") -> bool:
    """Prompt the user for confirmation.

    Args:
        message: The confirmation message to display.

    Returns:
        True if user confirms (y/yes), False otherwise.
    """
    user_input = input(f"{message} (y/N): ").strip().lower()
    return user_input in ("y", "yes")


def prompt_text(prompt_message: str) -> str:
    """Prompt the user to enter arbitrary text.

    Args:
        prompt_message: The message to display as the prompt.

    Returns:
        The entered text string (stripped of whitespace).
    """
    return input(prompt_message).strip()


def prompt_optional_text(prompt_message: str) -> str | None:
    """Prompt the user to enter optional text.

    Args:
        prompt_message: The message to display as the prompt.

    Returns:
        The entered text string, or None if skipped.
    """
    user_input = input(f"{prompt_message} (or press Enter to skip): ").strip()
    return user_input if user_input else None
