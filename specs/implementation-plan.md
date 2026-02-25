# Implementation Plan: Phase I Todo Application

**Document Version:** 1.0  
**Phase:** I (Console MVP)  
**Target:** Python 3.13+  
**Estimated Effort:** 5-7 days (single developer)  

---

## 1. Milestones Overview

| ID | Milestone | Estimated Effort | Dependencies |
|----|-----------|------------------|--------------|
| **M1** | Project Setup & Core Layer | 0.5 day | None |
| **M2** | Domain Layer Implementation | 1 day | M1 |
| **M3** | Infrastructure Layer Implementation | 0.5 day | M2 |
| **M4** | CLI Layer Implementation | 2 days | M2, M3 |
| **M5** | Application Entry Point & Integration | 0.5 day | M4 |
| **M6** | Testing & Quality Assurance | 1.5 days | M5 |
| **M7** | Documentation & Release Prep | 0.5 day | M6 |

---

## 2. Atomic Development Tasks

### Milestone M1: Project Setup & Core Layer

**Goal:** Establish project structure and implement shared utilities.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T1.1** | Create `src/` directory structure with all subdirectories (`cli/`, `domain/`, `infrastructure/`, `core/`) | 15 min | None |
| **T1.2** | Create `__init__.py` files in all packages | 10 min | T1.1 |
| **T1.3** | Implement `src/core/constants.py` with application constants | 20 min | None |
| **T1.4** | Implement `src/core/validators.py` with validation functions | 45 min | T1.3 |
| **T1.5** | Create `pyproject.toml` with project metadata and dependencies | 20 min | None |
| **T1.6** | Create `tests/` directory structure (`unit/`, `integration/`, `conftest.py`) | 15 min | None |

**Definition of Done (M1):**
- [ ] All directories and `__init__.py` files exist
- [ ] `constants.py` exports: `MAX_TITLE_LENGTH`, `MAX_DESCRIPTION_LENGTH`, `DEFAULT_PRIORITY`, `PRIORITY_LEVELS`, `DATE_FORMAT`
- [ ] `validators.py` exports: `validate_title()`, `validate_description()`, `validate_priority()`, `validate_date()`, `validate_task_id()`
- [ ] All validator functions have unit tests with ≥90% coverage
- [ ] `pyproject.toml` configured with pytest, ruff, mypy

**Git Commit Boundaries:**
```
commit 1: "chore: initialize project structure"
  - T1.1, T1.2, T1.5, T1.6

commit 2: "feat(core): implement constants and validators"
  - T1.3, T1.4
```

---

### Milestone M2: Domain Layer Implementation

**Goal:** Implement business entities and service layer.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T2.1** | Implement `src/domain/exceptions.py` with domain exception classes | 20 min | None |
| **T2.2** | Implement `src/domain/models.py` with `Priority` enum | 15 min | T1.3 |
| **T2.3** | Implement `src/domain/models.py` with `TaskStatus` enum | 15 min | T2.2 |
| **T2.4** | Implement `src/domain/models.py` with `Task` dataclass | 30 min | T2.2, T2.3 |
| **T2.5** | Implement `src/domain/services.py` with `TaskService` class skeleton | 20 min | T2.1, T2.4 |
| **T2.6** | Implement `TaskService.create_task()` method | 30 min | T2.5, T1.4 |
| **T2.7** | Implement `TaskService.get_all_tasks()` method | 20 min | T2.5 |
| **T2.8** | Implement `TaskService.get_task_by_id()` method | 20 min | T2.5 |
| **T2.9** | Implement `TaskService.update_task()` method | 30 min | T2.5, T1.4 |
| **T2.10** | Implement `TaskService.delete_task()` method | 20 min | T2.5 |
| **T2.11** | Implement `TaskService.toggle_completion()` method | 20 min | T2.5 |
| **T2.12** | Write unit tests for all domain models | 45 min | T2.4 |
| **T2.13** | Write unit tests for all service methods | 60 min | T2.6-T2.11 |

**Definition of Done (M2):**
- [ ] `Priority` enum with LOW, MEDIUM, HIGH values
- [ ] `TaskStatus` enum with ACTIVE, COMPLETED values
- [ ] `Task` dataclass with: id, title, description, priority, due_date, status, created_at
- [ ] `TaskService` class with all 6 CRUD methods implemented
- [ ] All domain exceptions defined: `TaskNotFoundError`, `ValidationError`, `DomainError`
- [ ] Unit tests pass with ≥95% coverage on domain layer
- [ ] Type hints present on all public methods
- [ ] mypy passes with strict mode

**Git Commit Boundaries:**
```
commit 3: "feat(domain): implement models and exceptions"
  - T2.1, T2.2, T2.3, T2.4

commit 4: "feat(domain): implement TaskService CRUD operations"
  - T2.5, T2.6, T2.7, T2.8, T2.9, T2.10, T2.11

commit 5: "test(domain): add unit tests for domain layer"
  - T2.12, T2.13
```

---

### Milestone M3: Infrastructure Layer Implementation

**Goal:** Implement in-memory data repository.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T3.1** | Implement `src/infrastructure/repositories.py` with `TaskRepository` abstract base class | 30 min | T2.4 |
| **T3.2** | Implement `InMemoryTaskRepository` class inheriting from `TaskRepository` | 45 min | T3.1 |
| **T3.3** | Implement `InMemoryTaskRepository.add()` method | 15 min | T3.2 |
| **T3.4** | Implement `InMemoryTaskRepository.get()` method | 15 min | T3.2 |
| **T3.5** | Implement `InMemoryTaskRepository.get_all()` method | 20 min | T3.2 |
| **T3.6** | Implement `InMemoryTaskRepository.update()` method | 20 min | T3.2 |
| **T3.7** | Implement `InMemoryTaskRepository.delete()` method | 15 min | T3.2 |
| **T3.8** | Write unit tests for repository implementation | 45 min | T3.3-T3.7 |

**Definition of Done (M3):**
- [ ] `TaskRepository` abstract base class defines interface: `add()`, `get()`, `get_all()`, `update()`, `delete()`
- [ ] `InMemoryTaskRepository` implements all methods using in-memory dictionary
- [ ] Repository methods raise `TaskNotFoundError` when appropriate
- [ ] Unit tests pass with ≥95% coverage on infrastructure layer
- [ ] Repository can be instantiated and used independently

**Git Commit Boundaries:**
```
commit 6: "feat(infrastructure): implement repository abstraction and in-memory implementation"
  - T3.1, T3.2, T3.3, T3.4, T3.5, T3.6, T3.7

commit 7: "test(infrastructure): add unit tests for repositories"
  - T3.8
```

---

### Milestone M4: CLI Layer Implementation

**Goal:** Implement console user interface components.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T4.1** | Implement `src/cli/formatters.py` with message formatting functions | 30 min | T1.3 |
| **T4.2** | Implement `src/cli/formatters.py` with task table formatting | 45 min | T4.1, T2.4 |
| **T4.3** | Implement `src/cli/formatters.py` with task detail formatting | 30 min | T4.1, T2.4 |
| **T4.4** | Implement `src/cli/prompts.py` with text input prompt function | 30 min | T1.4 |
| **T4.5** | Implement `src/cli/prompts.py` with selection prompt function | 25 min | T4.4 |
| **T4.6** | Implement `src/cli/prompts.py` with confirmation prompt function | 20 min | T4.4 |
| **T4.7** | Implement `src/cli/prompts.py` with date input prompt function | 25 min | T4.4, T1.4 |
| **T4.8** | Implement `src/cli/menus.py` with main menu display function | 25 min | T1.3 |
| **T4.9** | Implement `src/cli/menus.py` with menu selection handler | 30 min | T4.8 |
| **T4.10** | Implement `src/cli/app.py` with `TodoApp` class skeleton | 20 min | T2.5, T3.2 |
| **T4.11** | Implement `TodoApp.run()` main event loop | 30 min | T4.10, T4.9 |
| **T4.12** | Implement `TodoApp.handle_add_task()` method | 45 min | T4.4, T4.7, T2.6 |
| **T4.13** | Implement `TodoApp.handle_list_tasks()` method | 30 min | T4.2, T2.7 |
| **T4.14** | Implement `TodoApp.handle_update_task()` method | 45 min | T4.4, T4.5, T2.9 |
| **T4.15** | Implement `TodoApp.handle_delete_task()` method | 30 min | T4.6, T2.10 |
| **T4.16** | Implement `TodoApp.handle_toggle_completion()` method | 25 min | T4.6, T2.11 |
| **T4.17** | Implement `TodoApp.handle_view_details()` method | 25 min | T4.3, T2.8 |
| **T4.18** | Implement `TodoApp.handle_exit()` method | 10 min | T4.10 |
| **T4.19** | Write integration tests for CLI flows | 90 min | T4.12-T4.18 |

**Definition of Done (M4):**
- [ ] `formatters.py` exports: `format_success()`, `format_error()`, `format_info()`, `format_task_table()`, `format_task_detail()`
- [ ] `prompts.py` exports: `prompt_text()`, `prompt_selection()`, `prompt_confirmation()`, `prompt_date()`
- [ ] `menus.py` exports: `display_main_menu()`, `get_menu_selection()`
- [ ] `TodoApp` class with all 8 handler methods implemented
- [ ] Main menu displays all 7 options correctly
- [ ] All prompts validate input and re-prompt on invalid input
- [ ] Integration tests cover all user flows
- [ ] Manual testing confirms all CLI interactions work correctly

**Git Commit Boundaries:**
```
commit 8: "feat(cli): implement formatters and prompts"
  - T4.1, T4.2, T4.3, T4.4, T4.5, T4.6, T4.7

commit 9: "feat(cli): implement menus and main app structure"
  - T4.8, T4.9, T4.10, T4.11, T4.18

commit 10: "feat(cli): implement task operation handlers"
  - T4.12, T4.13, T4.14, T4.15, T4.16, T4.17

commit 11: "test(cli): add integration tests for CLI flows"
  - T4.19
```

---

### Milestone M5: Application Entry Point & Integration

**Goal:** Wire all components together and create executable entry point.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T5.1** | Implement `src/main.py` with application bootstrap | 20 min | T4.10 |
| **T5.2** | Implement dependency injection (repository → service → app) | 20 min | T5.1, T3.2, T2.5 |
| **T5.3** | Implement graceful shutdown handling (Ctrl+C) | 15 min | T5.1 |
| **T5.4** | Test full application flow end-to-end | 45 min | T5.1-T5.3 |
| **T5.5** | Fix integration issues between layers | 60 min | T5.4 |

**Definition of Done (M5):**
- [ ] `main.py` can be executed with `python src/main.py`
- [ ] Application starts and displays main menu
- [ ] All 7 menu options are functional
- [ ] Ctrl+C prompts for confirmation before exit
- [ ] No import errors or circular dependencies
- [ ] End-to-end manual testing passes all acceptance criteria

**Git Commit Boundaries:**
```
commit 12: "feat: implement application entry point and wire dependencies"
  - T5.1, T5.2, T5.3

commit 13: "fix: resolve integration issues between layers"
  - T5.5
```

---

### Milestone M6: Testing & Quality Assurance

**Goal:** Comprehensive testing and code quality verification.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T6.1** | Run full test suite and verify coverage | 30 min | M5 |
| **T6.2** | Add missing tests to reach coverage targets | 60 min | T6.1 |
| **T6.3** | Run ruff linter and fix all issues | 30 min | M5 |
| **T6.4** | Run mypy type checker and fix all issues | 45 min | M5 |
| **T6.5** | Perform manual acceptance testing against spec | 60 min | M5 |
| **T6.6** | Fix bugs discovered during testing | 60 min | T6.5 |
| **T6.7** | Re-run all tests and quality checks | 30 min | T6.6 |

**Definition of Done (M6):**
- [ ] Test coverage: ≥90% overall, ≥95% on domain layer
- [ ] ruff passes with zero errors
- [ ] mypy passes in strict mode with zero errors
- [ ] All acceptance criteria from specs verified manually
- [ ] Zero known bugs blocking release
- [ ] Test suite runs in under 30 seconds

**Git Commit Boundaries:**
```
commit 14: "test: add missing tests to reach coverage targets"
  - T6.2

commit 15: "chore: fix linting and type checking issues"
  - T6.3, T6.4

commit 16: "fix: resolve bugs from acceptance testing"
  - T6.6
```

---

### Milestone M7: Documentation & Release Prep

**Goal:** Finalize documentation and prepare for release.

| Task ID | Task Description | Estimated Time | Dependencies |
|---------|------------------|----------------|--------------|
| **T7.1** | Update `README.md` with installation and usage instructions | 30 min | M6 |
| **T7.2** | Add inline documentation (docstrings) to public APIs | 45 min | M6 |
| **T7.3** | Create `CHANGELOG.md` with initial release notes | 20 min | M6 |
| **T7.4** | Verify all specification documents are complete | 20 min | M6 |
| **T7.5** | Final git cleanup and tag creation | 15 min | T7.1-T7.4 |

**Definition of Done (M7):**
- [ ] `README.md` includes: project description, requirements, installation, usage examples
- [ ] All public classes and functions have docstrings
- [ ] `CHANGELOG.md` documents Phase I release
- [ ] All spec documents in `specs/` are complete and accurate
- [ ] Git repository is clean with meaningful commit history
- [ ] Release tag created (e.g., `v0.1.0-phase1`)

**Git Commit Boundaries:**
```
commit 17: "docs: update README and add docstrings"
  - T7.1, T7.2

commit 18: "docs: add CHANGELOG and finalize documentation"
  - T7.3, T7.4

commit 19: "chore: prepare release v0.1.0-phase1"
  - T7.5
```

---

## 3. Task Dependency Graph

```
T1.1 ──→ T1.2 ──┐
T1.5 ──────────→│
T1.6 ──────────→│
                │
                ▼
              T1.3 ──→ T1.4 ──┬──────────────┐
                              │              │
                              ▼              ▼
T2.1 ─────────────────────→ T2.5 ──→ T2.6 ──┐
T2.2 ──→ T2.3 ──→ T2.4 ──→ T2.5 ──┬─────────┤
                                  │         │
                                  ▼         ▼
T3.1 ──→ T3.2 ──┬──────────────→ T3.3     T4.10 ──→ T4.11
                │                │                  │
                ▼                ▼                  │
              T3.4             T3.5                 │
                │                │                  │
                ▼                ▼                  │
              T3.6             T3.7                 │
                │                │                  │
                └────────────────┴──────────────────┘
                              │
                              ▼
              T4.1 ──→ T4.2 ──┬──→ T4.3 ──┐
              T4.4 ──┬──→ T4.5 │          │
                     │        │          │
                     ├──→ T4.6 │          │
                     │        │          │
                     └──→ T4.7 │          │
                               │          │
                               ▼          ▼
                     T4.8 ──→ T4.9 ──→ T4.12 ──┐
                                               │
                                               ├──→ T5.4 ──→ T5.5
                                               │
                     T4.13 ──┐                 │
                     T4.14 ──┤                 │
                     T4.15 ──┼─────────────────┘
                     T4.16 ──┤
                     T4.17 ──┤
                     T4.18 ──┘
                               │
                               ▼
                             M6 ──→ M7
```

---

## 4. Execution Order Summary

| Order | Task ID | Milestone |
|-------|---------|-----------|
| 1 | T1.1, T1.2, T1.5, T1.6 | M1 |
| 2 | T1.3 | M1 |
| 3 | T1.4 | M1 |
| 4 | T2.1, T2.2, T2.3, T2.4 | M2 |
| 5 | T2.5, T2.6, T2.7, T2.8, T2.9, T2.10, T2.11 | M2 |
| 6 | T2.12, T2.13 | M2 |
| 7 | T3.1, T3.2, T3.3, T3.4, T3.5, T3.6, T3.7 | M3 |
| 8 | T3.8 | M3 |
| 9 | T4.1, T4.2, T4.3, T4.4, T4.5, T4.6, T4.7 | M4 |
| 10 | T4.8, T4.9, T4.10, T4.11, T4.18 | M4 |
| 11 | T4.12, T4.13, T4.14, T4.15, T4.16, T4.17 | M4 |
| 12 | T4.19 | M4 |
| 13 | T5.1, T5.2, T5.3 | M5 |
| 14 | T5.4, T5.5 | M5 |
| 15 | T6.1, T6.2, T6.3, T6.4, T6.5, T6.6, T6.7 | M6 |
| 16 | T7.1, T7.2, T7.3, T7.4, T7.5 | M7 |

---

## 5. Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| **R1:** Validator functions incomplete | Blocks domain layer | Implement validators first in M1; test thoroughly |
| **R2:** Repository interface changes | Breaks service layer | Define abstract base class before implementation |
| **R3:** CLI prompts don't handle edge cases | Poor user experience | Test with invalid inputs early; add robust error handling |
| **R4:** Integration issues between layers | Delays M5 | Run integration tests incrementally; don't wait until M5 |
| **R5:** Coverage targets not met | Blocks release | Write tests alongside implementation, not after |

---

## 6. Quality Gates

| Gate | Criteria | Checkpoint |
|------|----------|------------|
| **G1:** End of M1 | All validators pass unit tests | Before starting M2 |
| **G2:** End of M2 | Domain layer ≥95% coverage | Before starting M3 |
| **G3:** End of M3 | Repository tests pass | Before starting M4 |
| **G4:** End of M4 | All CLI flows work manually | Before starting M5 |
| **G5:** End of M5 | Full application runs without errors | Before starting M6 |
| **G6:** End of M6 | All quality checks pass | Before starting M7 |
| **G7:** End of M7 | Release ready | Before tagging |

---

## Appendix A: Commit Message Convention

All commits follow this format:

```
<type>(<scope>): <subject>

<body - optional>
```

| Type | Description |
|------|-------------|
| `feat` | New feature implementation |
| `fix` | Bug fix |
| `test` | Test additions or modifications |
| `docs` | Documentation changes |
| `chore` | Configuration, tooling, maintenance |

---

## Appendix B: Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-24 | — | Initial implementation plan |
