"""Output formatting functions for the CLI application."""

from datetime import datetime

from domain.models import Task, TaskStatus, Priority


SUCCESS_PREFIX = "✓"
ERROR_PREFIX = "✗"
INFO_PREFIX = "ℹ"


def format_success(message: str) -> str:
    """Format a success message.

    Args:
        message: The message to format.

    Returns:
        The formatted success message.
    """
    return f"{SUCCESS_PREFIX} {message}"


def format_error(message: str) -> str:
    """Format an error message.

    Args:
        message: The message to format.

    Returns:
        The formatted error message.
    """
    return f"{ERROR_PREFIX} Error: {message}"


def format_info(message: str) -> str:
    """Format an informational message.

    Args:
        message: The message to format.

    Returns:
        The formatted info message.
    """
    return f"{INFO_PREFIX} {message}"


def format_task_table(tasks: list[Task]) -> str:
    """Format a list of tasks as a table.

    Args:
        tasks: The list of tasks to format.

    Returns:
        A formatted table string.
    """
    if not tasks:
        return format_info("No tasks found.")

    column_widths = {
        "id": 4,
        "title": 24,
        "priority": 8,
        "due_date": 10,
        "status": 10,
    }

    header = (
        f"{'ID':<{column_widths['id']}} | "
        f"{'Title':<{column_widths['title']}} | "
        f"{'Priority':<{column_widths['priority']}} | "
        f"{'Due Date':<{column_widths['due_date']}} | "
        f"{'Status':<{column_widths['status']}}"
    )

    separator = "-" * len(header)

    lines = [header, separator]

    for task in tasks:
        title = _truncate(task.title, column_widths["title"])
        due_date = (
            task.due_date.strftime("%Y-%m-%d") if task.due_date else "-"
        )
        status = "Active" if task.status == TaskStatus.ACTIVE else "Completed"

        row = (
            f"{task.id:<{column_widths['id']}} | "
            f"{title:<{column_widths['title']}} | "
            f"{task.priority.value:<{column_widths['priority']}} | "
            f"{due_date:<{column_widths['due_date']}} | "
            f"{status:<{column_widths['status']}}"
        )
        lines.append(row)

    return "\n".join(lines)


def format_task_detail(task: Task) -> str:
    """Format a single task's full details.

    Args:
        task: The task to format.

    Returns:
        A formatted detail string.
    """
    status = "Active" if task.status == TaskStatus.ACTIVE else "Completed"
    due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "None"
    description = task.description if task.description else "None"
    created_at = task.created_at.strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "Task Details",
        "=" * 14,
        f"ID:          {task.id}",
        f"Title:       {task.title}",
        f"Description: {description}",
        f"Priority:    {task.priority.value}",
        f"Due Date:    {due_date}",
        f"Status:      {status}",
        f"Created At:  {created_at}",
    ]

    return "\n".join(lines)


def _truncate(text: str, max_length: int) -> str:
    """Truncate text to a maximum length with ellipsis.

    Args:
        text: The text to truncate.
        max_length: The maximum length.

    Returns:
        The truncated text with ellipsis if needed.
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
