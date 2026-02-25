# Feature Specification: Task CRUD Operations

**Document Version:** 1.0  
**Phase:** I (Console MVP)  
**Related Specification:** [specs/overview.md](../overview.md)  

---

## 1. User Stories

| ID | User Story | Priority |
|----|------------|----------|
| **US-1** | As a user, I want to create a new task with a title so that I can track items I need to accomplish | Must Have |
| **US-2** | As a user, I want to add an optional description to a task so that I can capture additional context | Should Have |
| **US-3** | As a user, I want to assign a priority level to a task so that I can focus on important items first | Must Have |
| **US-4** | As a user, I want to set an optional due date for a task so that I can track deadlines | Should Have |
| **US-5** | As a user, I want to view all my tasks in a formatted list so that I can see what needs to be done | Must Have |
| **US-6** | As a user, I want to filter tasks by status (active/completed) so that I can focus on pending work | Should Have |
| **US-7** | As a user, I want to update task details so that I can correct mistakes or reflect changes | Must Have |
| **US-8** | As a user, I want to delete tasks I no longer need so that my list stays relevant | Must Have |
| **US-9** | As a user, I want to mark tasks as complete or incomplete so that I can track my progress | Must Have |
| **US-10** | As a user, I want to view full details of a single task so that I can see all its attributes | Should Have |

---

## 2. Acceptance Criteria

### 2.1 Add Task (FR-1)

| ID | Criterion |
|----|-----------|
| **AC-1.1** | Given I am at the main menu, when I select "Add Task", then I am prompted to enter a task title |
| **AC-1.2** | Given I enter a non-empty title (≤200 characters), when I submit, then the task is created with a unique ID |
| **AC-1.3** | Given I enter an empty title, when I submit, then I see an error message and am prompted to re-enter |
| **AC-1.4** | Given I enter a title exceeding 200 characters, when I submit, then I see an error and am prompted to re-enter |
| **AC-1.5** | Given I am creating a task, when prompted, I can optionally enter a description |
| **AC-1.6** | Given I am creating a task, when prompted, I can select a priority level (Low/Medium/High) |
| **AC-1.7** | Given I do not specify a priority, when the task is created, then it defaults to "Medium" |
| **AC-1.8** | Given I am creating a task, when prompted, I can optionally enter a due date in YYYY-MM-DD format |
| **AC-1.9** | Given I enter an invalid date format, when I submit, then I see an error and can re-enter or skip |
| **AC-1.10** | Given I successfully create a task, when the task is saved, then I see a confirmation with the assigned task ID |

### 2.2 List Tasks (FR-2)

| ID | Criterion |
|----|-----------|
| **AC-2.1** | Given I am at the main menu, when I select "List Tasks", then all tasks are displayed in a formatted table |
| **AC-2.2** | Given there are no tasks, when I list tasks, then I see a message indicating no tasks exist |
| **AC-2.3** | Given tasks exist, when displayed, then each row shows: ID, Title, Priority, Due Date, Status |
| **AC-2.4** | Given tasks exist, when displayed, then they are sorted by priority (High→Medium→Low), then by creation time (oldest first) |
| **AC-2.5** | Given I am listing tasks, when prompted, I can filter by status: All, Active, or Completed |
| **AC-2.6** | Given I select "Active" filter, when tasks are displayed, then only incomplete tasks are shown |
| **AC-2.7** | Given I select "Completed" filter, when tasks are displayed, then only completed tasks are shown |
| **AC-2.8** | Given a task has no due date, when displayed, then the due date column shows "-" or "None" |
| **AC-2.9** | Given a task title exceeds display width, when displayed, then it is truncated with "..." indicator |

### 2.3 Update Task (FR-3)

| ID | Criterion |
|----|-----------|
| **AC-3.1** | Given I am at the main menu, when I select "Update Task", then I am prompted to enter a task ID |
| **AC-3.2** | Given I enter a non-existent task ID, when I submit, then I see an error and return to the main menu |
| **AC-3.3** | Given I enter an invalid task ID format, when I submit, then I see an error and am prompted to re-enter |
| **AC-3.4** | Given I enter a valid task ID, when I submit, then I see the current task details and update options |
| **AC-3.5** | Given I am updating a task, when I select an attribute to modify, then I can enter a new value |
| **AC-3.6** | Given I update the title, when I submit, then the new title must pass the same validation as creation |
| **AC-3.7** | Given I update the due date, when I submit, then the new date must be in YYYY-MM-DD format |
| **AC-3.8** | Given I make no changes, when I exit the update screen, then the task remains unchanged |
| **AC-3.9** | Given I successfully update a task, when the update completes, then I see a confirmation of changed fields |

### 2.4 Delete Task (FR-4)

| ID | Criterion |
|----|-----------|
| **AC-4.1** | Given I am at the main menu, when I select "Delete Task", then I am prompted to enter a task ID |
| **AC-4.2** | Given I enter a non-existent task ID, when I submit, then I see an error and return to the main menu |
| **AC-4.3** | Given I enter a valid task ID, when I submit, then I am asked to confirm the deletion |
| **AC-4.4** | Given I confirm deletion, when the operation completes, then the task is permanently removed |
| **AC-4.5** | Given I cancel deletion, when I respond negatively, then the task remains unchanged |
| **AC-4.6** | Given I successfully delete a task, when the operation completes, then I see a confirmation message |
| **AC-4.7** | Given I delete a task, when I list tasks afterward, then the deleted task no longer appears |

### 2.5 Mark Task Complete/Incomplete (FR-5)

| ID | Criterion |
|----|-----------|
| **AC-5.1** | Given I am at the main menu, when I select "Toggle Completion", then I am prompted to enter a task ID |
| **AC-5.2** | Given I enter a non-existent task ID, when I submit, then I see an error and return to the main menu |
| **AC-5.3** | Given I enter a valid task ID for an active task, when I submit, then the task is marked as completed |
| **AC-5.4** | Given I enter a valid task ID for a completed task, when I submit, then the task is marked as active |
| **AC-5.5** | Given I toggle a task's completion, when the operation completes, then I see a confirmation with the new status |
| **AC-5.6** | Given I complete a task, when I list tasks with "Active" filter, then the completed task no longer appears |

### 2.6 View Task Details (FR-6)

| ID | Criterion |
|----|-----------|
| **AC-6.1** | Given I am at the main menu, when I select "View Task Details", then I am prompted to enter a task ID |
| **AC-6.2** | Given I enter a non-existent task ID, when I submit, then I see an error and return to the main menu |
| **AC-6.3** | Given I enter a valid task ID, when I submit, then all task attributes are displayed |
| **AC-6.4** | Given a task is displayed, then the following are shown: ID, Title, Description, Priority, Due Date, Status, Created At |
| **AC-6.5** | Given a task has no description, when displayed, then the description field shows "None" or is omitted |

---

## 3. Validation Rules

### 3.1 Task Title

| Rule | Description | Error Message |
|------|-------------|---------------|
| **V-1.1** | Title must not be empty or whitespace only | "Error: Title cannot be empty." |
| **V-1.2** | Title must not exceed 200 characters | "Error: Title must not exceed 200 characters." |
| **V-1.3** | Title may contain any printable characters | — |

### 3.2 Task Description

| Rule | Description | Error Message |
|------|-------------|---------------|
| **V-2.1** | Description is optional | — |
| **V-2.2** | Description must not exceed 1000 characters | "Error: Description must not exceed 1000 characters." |

### 3.3 Task Priority

| Rule | Description | Error Message |
|------|-------------|---------------|
| **V-3.1** | Priority must be one of: Low, Medium, High | "Error: Priority must be Low, Medium, or High." |
| **V-3.2** | Priority is case-insensitive during input | — |
| **V-3.3** | Default priority is "Medium" if not specified | — |

### 3.4 Task Due Date

| Rule | Description | Error Message |
|------|-------------|---------------|
| **V-4.1** | Due date is optional | — |
| **V-4.2** | Due date must be in YYYY-MM-DD format | "Error: Date must be in YYYY-MM-DD format (e.g., 2026-02-24)." |
| **V-4.3** | Due date must be a valid calendar date | "Error: Invalid date. Please enter a valid date." |
| **V-4.4** | Due date may be in the past (no validation against current date) | — |

### 3.5 Task ID

| Rule | Description | Error Message |
|------|-------------|---------------|
| **V-5.1** | Task ID must be a positive integer | "Error: Task ID must be a positive number." |
| **V-5.2** | Task ID must reference an existing task | "Error: Task with ID {id} not found." |

---

## 4. Error Handling Requirements

### 4.1 Input Errors

| Error Type | Behavior | Recovery |
|------------|----------|----------|
| **Empty Input** | Display specific error message; re-prompt for input | User can re-enter or cancel with Ctrl+C |
| **Invalid Format** | Display error with expected format example; re-prompt | User can re-enter or skip (if optional) |
| **Out of Range** | Display error with valid range; re-prompt | User can re-enter |
| **Non-existent Reference** | Display error with context; return to menu | User can retry from main menu |

### 4.2 System Errors

| Error Type | Behavior | Recovery |
|------------|----------|----------|
| **Unexpected Exception** | Display generic error message; log traceback internally; return to main menu | Application remains running; user can continue |
| **Terminal Interrupt (Ctrl+C)** | Display confirmation prompt: "Exit without saving?" | User can confirm exit or cancel |
| **Terminal Resize** | Redraw interface on next input/output cycle | Automatic |

### 4.3 Error Message Guidelines

| Principle | Description |
|-----------|-------------|
| **Clarity** | Messages must clearly state what went wrong |
| **Actionability** | Messages must indicate how to resolve the issue |
| **Tone** | Messages must be neutral and non-judgmental |
| **Consistency** | Error format: "Error: {description}. {guidance}" |

---

## 5. CLI Interaction Behavior

### 5.1 Main Menu

```
=== Todo Application ===
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Toggle Completion
6. View Task Details
7. Exit

Select an option (1-7):
```

| Behavior | Description |
|----------|-------------|
| **Invalid Menu Selection** | Display "Error: Please enter a number between 1 and 7."; re-prompt |
| **Non-numeric Input** | Display "Error: Please enter a valid number."; re-prompt |
| **Exit Selection** | Display "Goodbye!"; terminate application |

### 5.2 Input Prompts

| Prompt Type | Format | Example |
|-------------|--------|---------|
| **Required Text** | `Enter {field}: ` | `Enter title: ` |
| **Optional Text** | `Enter {field} (or press Enter to skip): ` | `Enter description (or press Enter to skip): ` |
| **Selection** | `Select {option} ({choices}): ` | `Select priority (Low/Medium/High): ` |
| **Confirmation** | `Are you sure? (y/N): ` | `Are you sure? (y/N): ` |
| **Numeric ID** | `Enter {entity} ID: ` | `Enter task ID: ` |

### 5.3 Output Formatting

| Element | Format |
|---------|--------|
| **Success Message** | `✓ {description}` |
| **Error Message** | `✗ Error: {description}` |
| **Info Message** | `ℹ {description}` |
| **Task List Table** | Aligned columns with headers; borders optional |
| **Task Detail View** | Key-value pairs, one per line |

### 5.4 Task List Display

```
ID  | Title                    | Priority | Due Date   | Status
----|--------------------------|----------|------------|----------
1   | Complete project proposal| High     | 2026-02-25 | Active
3   | Review team feedback     | Medium   | -          | Active
2   | Send weekly report       | Low      | 2026-02-28 | Completed
```

| Behavior | Description |
|----------|-------------|
| **Title Truncation** | Titles > 24 characters truncated to 21 chars + "..." |
| **Empty State** | Display "ℹ No tasks found." when list is empty |
| **Filter Applied** | Display "ℹ Showing {filter} tasks only." above table |

### 5.5 Task Detail Display

```
Task Details
============
ID:          1
Title:       Complete project proposal
Description: Submit the Q1 project proposal to the steering committee
Priority:    High
Due Date:    2026-02-25
Status:      Active
Created At:  2026-02-24 10:30:00
```

| Behavior | Description |
|----------|-------------|
| **Missing Description** | Display "Description: None" |
| **Missing Due Date** | Display "Due Date: None" |

### 5.6 Navigation Flow

```
┌─────────────┐
│  Main Menu  │
└──────┬──────┘
       │
       ├──→ Add Task ──→ Confirm ──→ Main Menu
       ├──→ List Tasks ─→ Display ──→ Main Menu
       ├──→ Update Task ─→ Confirm ──→ Main Menu
       ├──→ Delete Task ─→ Confirm ──→ Main Menu
       ├──→ Toggle Completion ─→ Confirm ──→ Main Menu
       ├──→ View Details ─→ Display ──→ Main Menu
       └──→ Exit ──→ Terminate
```

| Behavior | Description |
|----------|-------------|
| **Post-Action Flow** | After any operation completes, return to main menu |
| **Cancel Behavior** | User can cancel any operation and return to main menu |
| **No Deep Nesting** | Maximum menu depth is 2 levels (main → operation → confirm) |

---

## Appendix A: State Transitions

### Task Status Lifecycle

```
     ┌──────────────┐
     │   Created    │
     │   (Active)   │
     └──────┬───────┘
            │
      ┌─────┴─────┐
      │           │
      ▼           ▼
┌──────────┐ ┌────────────┐
│ Completed│ │  Deleted   │
│          │ │ (Terminal) │
└────┬─────┘ └────────────┘
     │
     │ (toggle)
     │
     ▼
┌──────────────┐
│   Active     │
│ (reverted)   │
└──────────────┘
```

---

## Appendix B: Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-24 | — | Initial feature specification for Task CRUD |
