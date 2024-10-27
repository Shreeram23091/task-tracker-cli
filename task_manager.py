import sys
import os

TASK_FILE_PATH = "tasks.txt"

def load_tasks():
    """Reads tasks from the specified file and returns them as a list of dictionaries."""
    if not os.path.exists(TASK_FILE_PATH):
        return []
    with open(TASK_FILE_PATH, "r") as file:
        tasks = [line.strip().split(", ", 1) for line in file]
        return [{"status": status, "description": description} for status, description in tasks]

def save_tasks(tasks):
    """Writes the list of tasks to the specified file."""
    with open(TASK_FILE_PATH, "w") as file:
        for task in tasks:
            file.write(f"{task['status']}, {task['description']}\n")

def add_task(description):
    """Appends a new task with 'pending' status to the task list and saves it."""
    tasks = load_tasks()
    tasks.append({"status": "pending", "description": description})
    save_tasks(tasks)
    print(f"Added new task: {description}")

def list_tasks():
    """Show all tasks, separated by pending and completed categories."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("Pending Tasks:")
        for index, task in enumerate(tasks, start=1):
            if task["status"] == "pending":
                print(f"{index}. {task['description']}")

        print("\nCompleted Tasks:")
        for index, task in enumerate(tasks, start=1):
            if task["status"] == "completed":
                print(f"{index}. {task['description']}")

def complete_task(task_number):
    """Set a task as completed based on its assigned number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        if task["status"] == "pending":
            task["status"] = "completed"
            save_tasks(tasks)
            print(f"Task marked as completed: {task['description']}")
        else:
            print("This task has already been completed.")
    else:
        print("The task number provided is invalid.")


def delete_task(task_number):
    """delete a task using its assigned number."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task deleted: {task['description']}")
    else:
        print("The task number provided is invalid.")

def main():
    """Process command-line arguments and invoke the corresponding function."""
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
