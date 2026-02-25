# Architecture Specification: Phase I Todo Application

**Document Version:** 1.0  
**Phase:** I (Console MVP)  
**Target:** Python 3.13+  

---

## 1. Overview

This document defines the software architecture for the Phase I Todo application. The architecture prioritizes:

- **Separation of Concerns** – Clear boundaries between UI, business logic, and data layers
- **Testability** – Each layer can be tested in isolation
- **Extensibility** – Minimal changes required when adding persistence or web interfaces in Phase II+
- **Simplicity** – No over-engineering for Phase I requirements

---

## 2. Proposed Folder Structure

```
/home/abeer/hackathon-todo/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   │
│   ├── cli/                    # CLI Layer (Presentation)
│   │   ├── __init__.py
│   │   ├── app.py              # Main CLI application controller
│   │   ├── menus.py            # Menu rendering and navigation
│   │   ├── prompts.py          # Input prompts and validation
│   │   └── formatters.py       # Output formatting (tables, messages)
│   │
│   ├── domain/                 # Domain Layer (Business Logic)
│   │   ├── __init__.py
│   │   ├── models.py           # Task entity and value objects
│   │   ├── services.py         # Task CRUD service (business rules)
│   │   └── exceptions.py       # Domain-specific exceptions
│   │
│   ├── infrastructure/         # Infrastructure Layer (Data Access)
│   │   ├── __init__.py
│   │   └── repositories.py     # In-memory task repository
│   │
│   └── core/                   # Core Layer (Shared Utilities)
│       ├── __init__.py
│       ├── validators.py       # Input validation functions
│       └── constants.py        # Application-wide constants
│
├── tests/                      # Test Suite
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_domain.py
│   │   ├── test_services.py
│   │   └── test_repositories.py
│   ├── integration/
│   │   └── test_cli_flow.py
│   └── conftest.py             # Pytest fixtures
│
├── specs/                      # Specifications (existing)
├── README.md
├── constitution.md
└── pyproject.toml              # Project configuration
```

---

## 3. Module Responsibilities

### 3.1 Entry Point

| Module | `src/main.py` |
|--------|---------------|
| **Responsibility** | Application bootstrap and lifecycle management |
| **Dependencies** | `cli.app` |
| **Functions** | - Initialize application components<br>- Start CLI event loop<br>- Handle graceful shutdown |
| **Future Changes** | None expected; may delegate to web server in Phase II |

---

### 3.2 CLI Layer (`src/cli/`)

| Module | `src/cli/app.py` |
|--------|------------------|
| **Responsibility** | Main CLI controller; orchestrates user interaction flow |
| **Dependencies** | `cli.menus`, `cli.prompts`, `domain.services` |
| **Functions** | - Route menu selections to appropriate handlers<br>- Invoke service methods<br>- Display results and errors |
| **Future Changes** | May be replaced or supplemented by web controllers in Phase II |

| Module | `src/cli/menus.py` |
|--------|---------------------|
| **Responsibility** | Render menu interfaces and handle navigation |
| **Dependencies** | `cli.formatters`, `core.constants` |
| **Functions** | - Display main menu and sub-menus<br>- Parse menu selections<br>- Handle invalid input |
| **Future Changes** | Not applicable to web architecture |

| Module | `src/cli/prompts.py` |
|--------|----------------------|
| **Responsibility** | Handle user input prompts with validation |
| **Dependencies** | `core.validators` |
| **Functions** | - Prompt for text input with validation<br>- Prompt for selection from options<br>- Handle cancellation (Ctrl+C) |
| **Future Changes** | Web forms will replace console prompts in Phase II |

| Module | `src/cli/formatters.py` |
|--------|-------------------------|
| **Responsibility** | Format output for console display |
| **Dependencies** | `core.constants` |
| **Functions** | - Format task lists as tables<br>- Format success/error/info messages<br>- Truncate text for display |
| **Future Changes** | Replaced by JSON/HTML rendering in Phase II |

---

### 3.3 Domain Layer (`src/domain/`)

| Module | `src/domain/models.py` |
|--------|------------------------|
| **Responsibility** | Define domain entities and value objects |
| **Dependencies** | `core.constants`, standard library (`dataclasses`, `datetime`, `uuid`, `enum`) |
| **Classes** | - `Task` – Main entity with id, title, description, priority, due_date, status, created_at<br>- `Priority` – Enum (LOW, MEDIUM, HIGH)<br>- `TaskStatus` – Enum (ACTIVE, COMPLETED) |
| **Future Changes** | May add fields (tags, subtasks) in future phases |

| Module | `src/domain/services.py` |
|--------|--------------------------|
| **Responsibility** | Implement business logic for task operations |
| **Dependencies** | `domain.models`, `domain.exceptions`, `infrastructure.repositories` |
| **Functions** | - `create_task()` – Validate and create new task<br>- `get_all_tasks()` – Retrieve tasks with optional filtering<br>- `get_task_by_id()` – Retrieve single task<br>- `update_task()` – Modify task attributes<br>- `delete_task()` – Remove task<br>- `toggle_completion()` – Change task status |
| **Future Changes** | Business rules remain stable; may add new operations |

| Module | `src/domain/exceptions.py` |
|--------|----------------------------|
| **Responsibility** | Define domain-specific exception classes |
| **Dependencies** | None (standard library only) |
| **Classes** | - `TaskNotFoundError` – Task ID does not exist<br>- `ValidationError` – Input validation failed<br>- `DomainError` – Base class for domain exceptions |
| **Future Changes** | May add more specific exceptions as needed |

---

### 3.4 Infrastructure Layer (`src/infrastructure/`)

| Module | `src/infrastructure/repositories.py` |
|--------|--------------------------------------|
| **Responsibility** | Abstract data access; implement in-memory storage |
| **Dependencies** | `domain.models`, `domain.exceptions` |
| **Classes** | - `TaskRepository` – Abstract base class (interface)<br>- `InMemoryTaskRepository` – Concrete implementation using dict |
| **Functions** | - `add()`, `get()`, `get_all()`, `update()`, `delete()` |
| **Future Changes** | New implementations (SQLite, PostgreSQL, etc.) can be added without modifying domain layer |

---

### 3.5 Core Layer (`src/core/`)

| Module | `src/core/validators.py` |
|--------|--------------------------|
| **Responsibility** | Provide reusable validation functions |
| **Dependencies** | `core.constants`, standard library (`re`, `datetime`) |
| **Functions** | - `validate_title()` – Non-empty, max length<br>- `validate_description()` – Max length<br>- `validate_priority()` – Valid enum value<br>- `validate_date()` – YYYY-MM-DD format<br>- `validate_task_id()` – Positive integer |
| **Future Changes** | May add more validators as features expand |

| Module | `src/core/constants.py` |
|--------|-------------------------|
| **Responsibility** | Define application-wide constants |
| **Dependencies** | None |
| **Constants** | - `MAX_TITLE_LENGTH = 200`<br>- `MAX_DESCRIPTION_LENGTH = 1000`<br>- `DEFAULT_PRIORITY = "MEDIUM"`<br>- `DATE_FORMAT = "%Y-%m-%d"` |
| **Future Changes** | May add more constants as needed |

---

## 4. Data Flow Description

### 4.1 Create Task Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CLI App   │────▶│   Prompts   │────▶│ Validators  │
│ (app.py)    │     │ (prompts.py)│     │ (validators)│
└──────┬──────┘     └─────────────┘     └─────────────┘
       │
       │ (validated input)
       ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Service   │────▶│  Repository │────▶│   Models    │
│ (services)  │     │ (in-memory) │     │  (Task)     │
└──────┬──────┘     └─────────────┘     └─────────────┘
       │
       │ (created task)
       ▼
┌─────────────┐
│  Formatters │
│(formatters.py)
└─────────────┘
```

**Step-by-step:**
1. `app.py` receives "Add Task" menu selection
2. `prompts.py` collects title, description, priority, due date
3. `validators.py` validates each input; re-prompts on failure
4. `services.py` creates `Task` entity via repository
5. `repository.py` stores task in memory dictionary
6. `formatters.py` displays success message with task ID

### 4.2 List Tasks Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CLI App   │────▶│   Service   │────▶│  Repository │
│ (app.py)    │     │ (services)  │     │ (in-memory) │
└──────┬──────┘     └──────┬──────┘     └─────────────┘
       │                   │
       │                   │ (filter, sort)
       │                   ▼
       │             ┌─────────────┐
       │             │   Models    │
       │             │  (Task[])   │
       │             └─────────────┘
       │
       ▼
┌─────────────┐
│  Formatters │
│(formatters.py)
└─────────────┘
```

### 4.3 Error Propagation Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Repository │────▶│  Exceptions │────▶│   Service   │
│             │     │  (raise)    │     │  (catch/    │
│             │     │             │     │  re-raise)  │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
┌─────────────┐                         ┌─────────────┐
│  Formatters │◀────────────────────────│   CLI App   │
│(display err)│                         │  (handle)   │
└─────────────┘                         └─────────────┘
```

---

## 5. Dependency Boundaries

### 5.1 Dependency Graph

```
                    ┌─────────────┐
                    │   main.py   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   cli/      │
                    │   app.py    │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │ cli/menus.py│ │cli/prompts.py│ │cli/format-  │
    │             │ │             │ │ters.py      │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
           └───────────────┼───────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  domain/    │
                    │  services.py│
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
           ▼               ▼               ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │domain/      │ │domain/      │ │infrastructure/
    │models.py    │ │exceptions.py│ │repositories.py
    └──────┬──────┘ └─────────────┘ └──────┬──────┘
           │                               │
           └───────────────┬───────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   core/     │
                    │ validators  │
                    │ constants   │
                    └─────────────┘
```

### 5.2 Dependency Rules

| Rule | Description | Enforcement |
|------|-------------|-------------|
| **D-1** | `cli` depends on `domain` (not vice versa) | Import checks |
| **D-2** | `domain` depends on `infrastructure` only via abstraction | Repository interface |
| **D-3** | `infrastructure` depends on `domain` (for models) | Acceptable; no business logic |
| **D-4** | `core` has no dependencies on other layers | Pure utilities |
| **D-5** | `domain` has no dependencies on `cli` | Ensures business logic portability |
| **D-6** | All layers may depend on `core` | Shared utilities |

### 5.3 Inversion Points

| Interface | Purpose | Implementation |
|-----------|---------|----------------|
| `TaskRepository` (abstract) | Data access abstraction | `InMemoryTaskRepository` (Phase I)<br>`SQLiteTaskRepository` (Phase II)<br>`PostgresTaskRepository` (Phase III) |

---

## 6. Future Extensibility

### 6.1 Phase II: Database Persistence

| Change | Description |
|--------|-------------|
| **New Module** | `infrastructure/sqlite_repository.py` – SQLite implementation of `TaskRepository` |
| **Modified Module** | `main.py` – Inject SQLite repository instead of in-memory |
| **Unchanged** | `domain/`, `cli/` (business logic and UI remain the same) |

### 6.2 Phase III: Web Interface

| Change | Description |
|--------|-------------|
| **New Layer** | `web/` – FastAPI routes, request/response models, HTML templates |
| **Modified Module** | `main.py` – Start web server instead of CLI (or both) |
| **Unchanged** | `domain/`, `infrastructure/` (business logic and data access remain the same) |

### 6.3 Phase IV: Authentication & Multi-User

| Change | Description |
|--------|-------------|
| **New Module** | `domain/user_models.py`, `domain/auth_service.py` |
| **Modified Module** | `domain/models.py` – Add `owner_id` to Task<br>`infrastructure/` – Add user filtering to queries |
| **Unchanged** | Core CRUD operations remain valid |

---

## 7. Testing Strategy

| Layer | Test Type | Tools | Coverage Target |
|-------|-----------|-------|-----------------|
| `domain/` | Unit tests | pytest | 100% |
| `infrastructure/` | Unit tests | pytest | 95% |
| `cli/` | Integration tests | pytest + input mocking | 90% |
| End-to-end | Flow tests | pytest | Critical paths |

---

## Appendix A: Design Patterns

| Pattern | Usage |
|---------|-------|
| **Repository** | `TaskRepository` abstracts data access |
| **Service Layer** | `TaskService` encapsulates business logic |
| **Dependency Injection** | Repository injected into service; service injected into CLI app |
| **Single Responsibility** | Each module has one clear purpose |
| **Open/Closed** | New repository implementations can be added without modifying existing code |

---

## Appendix B: Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-24 | — | Initial architecture specification |
