"""Application entrypoint for the Todo CLI application."""

import sys

from domain.services import TaskService
from infrastructure.sqlite_repository import SQLiteTaskRepository
from cli.controller import CLIController
from infrastructure.database import init_database


def main() -> None:
    """Bootstrap and run the Todo CLI application.

    This function wires together all application dependencies:
    1. Creates the SQLite repository
    2. Creates the task service with the repository
    3. Creates the CLI controller with the service
    4. Starts the main event loop
    """
    init_database()
    repository = SQLiteTaskRepository()
    service = TaskService(repository)
    controller = CLIController(service)

    try:
        controller.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
