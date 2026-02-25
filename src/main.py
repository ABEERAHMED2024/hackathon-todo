"""Application entrypoint for the Todo CLI application."""

from domain.services import TaskService
from infrastructure.in_memory_repository import InMemoryTaskRepository
from cli.controller import CLIController


def main() -> None:
    """Bootstrap and run the Todo CLI application.

    This function wires together all application dependencies:
    1. Creates the in-memory repository
    2. Creates the task service with the repository
    3. Creates the CLI controller with the service
    4. Starts the main event loop
    """
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    controller = CLIController(service)

    controller.run()


if __name__ == "__main__":
    main()
