# Task Manager CLI Tool

A straightforward command-line interface (CLI) application for managing tasks, enabling users to add, view, complete, and delete tasks. Tasks are saved in a text file (`tasks.txt`) to ensure they persist across sessions.

## Features
- **Add a Task**: Users can add a new task with a description.
- **View Tasks**: Users can view all pending tasks.
- **Complete a Task**: Users can mark a task as completed, which removes it from the list.
- **Delete a Task**: Users can delete a task by its number.

## Installation

1. **Clone the Repository**:
   Open your terminal or command prompt and run:
   ```bash
   https://github.com/Shreeram23091/CLI-Task-Manager
   cd CLI-Task-Manager
   ```

2. **Run the Script**: Ensure you have Python installed. In the same terminal or command prompt, run the script using:
   ```bash
   python task_manager.py
   ```

## Usage

### Add a Task
To add a task, use the following command:
```bash
python task_manager.py add "Your task description"
```
**Example**:
```bash
python task_manager.py add "Buy groceries"
```

### View Tasks
To view all pending tasks, run:
```bash
python task_manager.py list
```

### Complete a Task
To mark a task as completed, use:
```bash
python task_manager.py complete [task number]
```
**Example**:
```bash
python task_manager.py complete 1
```

### Delete a Task
To delete a task by its number, run:
```bash
python task_manager.py delete [task number]
```
**Example**:
```bash
python task_manager.py delete 1
```

## Error Handling
If an invalid task number is entered for completing or deleting a task, the program will display an error message indicating that the task number is not valid.

## Sample `tasks.txt` Format
Each line in `tasks.txt` represents a task:
```
Buy groceries
Finish homework
Read a book
```