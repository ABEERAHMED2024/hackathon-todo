"""Main CLI controller for the Todo application."""

from datetime import datetime

from domain.exceptions import TaskNotFoundError, ValidationError
from domain.models import TaskStatus, Priority
from domain.services import TaskService

from cli.menu import MenuOption, display_main_menu, get_menu_selection
from cli import input_handler
from cli.output_formatter import (
    format_success,
    format_error,
    format_info,
    format_task_table,
    format_task_detail,
)


class CLIController:
    """Main controller for the CLI application.

    This class orchestrates user interaction by:
    - Displaying menus and prompts
    - Calling TaskService methods
    - Formatting and displaying results
    - Handling domain exceptions gracefully

    Attributes:
        service: The TaskService instance for business logic.
    """

    def __init__(self, service: TaskService) -> None:
        """Initialize the controller with a TaskService.

        Args:
            service: The TaskService instance to use for operations.
        """
        self._service = service

    def run(self) -> None:
        """Run the main CLI event loop.

        Continuously displays the menu and handles user selections
        until the user chooses to exit.
        """
        while True:
            display_main_menu()
            selection = get_menu_selection()

            if selection is None:
                print(format_error("Please enter a number between 1 and 7."))
                continue

            if selection == MenuOption.EXIT:
                print(format_info("Goodbye!"))
                break

            self._handle_selection(selection)

    def _handle_selection(self, selection: MenuOption) -> None:
        """Route a menu selection to the appropriate handler.

        Args:
            selection: The selected menu option.
        """
        handlers = {
            MenuOption.ADD_TASK: self._handle_add_task,
            MenuOption.LIST_TASKS: self._handle_list_tasks,
            MenuOption.UPDATE_TASK: self._handle_update_task,
            MenuOption.DELETE_TASK: self._handle_delete_task,
            MenuOption.TOGGLE_COMPLETION: self._handle_toggle_completion,
            MenuOption.VIEW_DETAILS: self._handle_view_details,
        }

        handler = handlers.get(selection)
        if handler:
            try:
                handler()
            except ValidationError as e:
                print(format_error(str(e)))
            except TaskNotFoundError as e:
                print(format_error(str(e)))
            except ValueError as e:
                print(format_error(str(e)))
            except KeyboardInterrupt:
                print(format_info("\nOperation cancelled."))

    def _handle_add_task(self) -> None:
        """Handle the Add Task operation."""
        try:
            title = input_handler.prompt_title()
            description = input_handler.prompt_description()
            priority = input_handler.prompt_priority() or "MEDIUM"
            due_date = input_handler.prompt_due_date()

            task = self._service.create_task(
                title=title,
                description=description,
                priority=priority,
                due_date=due_date,
            )

            print(format_success(f"Task created with ID: {task.id}"))

        except ValueError as e:
            print(format_error(str(e)))

    def _handle_list_tasks(self) -> None:
        """Handle the List Tasks operation."""
        print("\nFilter by status:")
        print("1. All")
        print("2. Active")
        print("3. Completed")

        try:
            filter_choice = input("Select filter (1-3, or Enter for All): ").strip()

            status_filter = None
            if filter_choice == "2":
                status_filter = TaskStatus.ACTIVE
            elif filter_choice == "3":
                status_filter = TaskStatus.COMPLETED

            tasks = self._service.get_all_tasks(status=status_filter)
            print(format_task_table(tasks))

        except ValueError:
            print(format_error("Invalid selection."))

    def _handle_update_task(self) -> None:
        """Handle the Update Task operation."""
        try:
            task_id = input_handler.prompt_task_id()
            task = self._service.get_task_by_id(task_id)

            print(format_task_detail(task))
            print("\nWhat would you like to update?")
            print("1. Title")
            print("2. Description")
            print("3. Priority")
            print("4. Due Date")
            print("5. Cancel")

            choice = input("Select option (1-5): ").strip()

            if choice == "5":
                print(format_info("Update cancelled."))
                return

            title = None
            description = None
            priority = None
            due_date = None

            if choice == "1":
                title = input_handler.prompt_title()
            elif choice == "2":
                description = input_handler.prompt_optional_text("Enter new description")
            elif choice == "3":
                priority = input_handler.prompt_priority()
            elif choice == "4":
                due_date_str = input("Enter new due date (YYYY-MM-DD): ").strip()
                if due_date_str:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

            updated_task = self._service.update_task(
                task_id=task_id,
                title=title,
                description=description,
                priority=priority,
                due_date=due_date,
            )

            print(format_success(f"Task {updated_task.id} updated successfully."))

        except ValueError as e:
            print(format_error(str(e)))

    def _handle_delete_task(self) -> None:
        """Handle the Delete Task operation."""
        try:
            task_id = input_handler.prompt_task_id()

            task = self._service.get_task_by_id(task_id)
            print(f"Task to delete: {task.title}")

            if input_handler.prompt_confirmation("Delete this task"):
                self._service.delete_task(task_id)
                print(format_success(f"Task {task_id} deleted."))
            else:
                print(format_info("Deletion cancelled."))

        except ValueError:
            print(format_error("Invalid task ID."))

    def _handle_toggle_completion(self) -> None:
        """Handle the Toggle Completion operation."""
        try:
            task_id = input_handler.prompt_task_id()

            task = self._service.toggle_completion(task_id)
            status = "completed" if task.status == TaskStatus.COMPLETED else "active"

            print(format_success(f"Task {task_id} marked as {status}."))

        except ValueError:
            print(format_error("Invalid task ID."))

    def _handle_view_details(self) -> None:
        """Handle the View Task Details operation."""
        try:
            task_id = input_handler.prompt_task_id()

            task = self._service.get_task_by_id(task_id)
            print(format_task_detail(task))

        except ValueError:
            print(format_error("Invalid task ID."))
