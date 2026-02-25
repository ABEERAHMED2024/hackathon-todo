"""Menu display and navigation for the CLI application."""

from enum import IntEnum


class MenuOption(IntEnum):
    """Main menu options."""

    ADD_TASK = 1
    LIST_TASKS = 2
    UPDATE_TASK = 3
    DELETE_TASK = 4
    TOGGLE_COMPLETION = 5
    VIEW_DETAILS = 6
    EXIT = 7


MENU_TITLE = "=== Todo Application ==="

MENU_OPTIONS = """1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. View Task Details
7. Exit"""

PROMPT_SELECTION = "Select an option (1-7): "


def display_main_menu() -> None:
    """Display the main menu to the user."""
    print(f"\n{MENU_TITLE}")
    print(MENU_OPTIONS)


def get_menu_selection() -> MenuOption | None:
    """Get and validate menu selection from user.

    Returns:
        The selected MenuOption, or None if user wants to exit.
    """
    try:
        user_input = input(PROMPT_SELECTION).strip()
        if not user_input:
            return None
        selection = int(user_input)
        return MenuOption(selection)
    except (ValueError, KeyError):
        return None
