# Task Manager CLI Tool

A simple command-line interface (CLI) application designed for managing tasks. Users can add, view, complete, and delete tasks, with all data stored in a text file (`tasks.txt`) for persistence across sessions.

## Features
- **Add a Task**: Easily append new tasks with a description, marked as "pending."
- **View Tasks**: Display all tasks, categorized into pending and completed.
- **Complete a Task**: Mark a specified task as completed.
- **Delete a Task**: delete a task from the list by its assigned number.

## Modules Used
- **`sys`**: This built-in module provides access to system-specific parameters and functions. It allows the program to read user input from the command line, facilitating interaction with the task manager.
- **`os`**: This built-in module offers a way to use operating system-dependent functionality, such as checking the existence of files. It ensures the application can load tasks from a file or create a new one if it doesn’t exist.

## Installation

1. **Clone the Repository**:  
   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/Shreeram23091/task-tracker-cli
   cd task-tracker-cli
   ```

2. **Run the Script**:  
   Ensure you have Python installed. In the same terminal or command prompt, execute the script using:
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
python task_manager.py add "Buy Grocery"
```

### View All Tasks
To view all tasks (both pending and completed), run:
```bash
python task_manager.py list
```
**Example Output**:
```
Pending Tasks:
1. Buy book
3. Read a Book

Completed Tasks:
2. Buy Grocery
```

### Complete a Task
To mark a task as completed, use:
```bash
python task_manager.py complete [task number]
```
**Example**:
```bash
python task_manager.py complete 2
```

### Delete a Task
To delete a task by its number, run:
```bash
python task_manager.py delete [task number]
```
**Example**:
```bash
python task_manager.py delete 3
```

## Error Handling
If an invalid task number is provided for completing or deleting a task, the program will display an error message indicating that the task number is invalid.

## Sample `tasks.txt` Format
Each line in `tasks.txt` represents a task in the following format:
```
status, description
```
**Example**:
```
pending, Buy groceries
completed, Finish homework
pending, Read a book
```