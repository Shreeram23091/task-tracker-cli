import sys
import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from the file and return a list of task dictionaries."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        tasks = [line.strip().split(", ", 1) for line in file.readlines()]
        return [{"status": status, "description": description} for status, description in tasks]

def save_tasks(tasks):
    """Save the current list of tasks to the file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['status']}, {task['description']}\n")

def add_task(description):
    """Add a new task with a pending status."""
    tasks = load_tasks()
    tasks.append({"status": "pending", "description": description})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """Display all tasks, grouped by pending and completed status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Pending Tasks:")
        for i, task in enumerate(tasks, 1):
            if task["status"] == "pending":
                print(f"{i}. {task['description']}")

        print("\nCompleted Tasks:")
        for i, task in enumerate(tasks, 1):
            if task["status"] == "completed":
                print(f"{i}. {task['description']}")

def complete_task(task_number):
    """Mark a task as completed based on its number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        if task["status"] == "pending":
            task["status"] = "completed"
            save_tasks(tasks)
            print(f"Task completed: {task['description']}")
        else:
            print("Task is already marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete a task by its number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task deleted: {task['description']}")
    else:
        print("Invalid task number.")

def main():
    """Parse command-line arguments and execute the corresponding function."""
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py [add|list|complete|delete] [arguments...]")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
    elif command == "list":
        list_tasks()
    elif command == "complete" and len(sys.argv) == 3:
        complete_task(int(sys.argv[2]))
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()
