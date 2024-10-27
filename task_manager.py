import sys
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip().split(", ", 1) for line in file.readlines()]
        return [{"status": status, "description": description} for status, description in tasks]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['status']}, {task['description']}\n")

def add_task(description):
    tasks = load_tasks()
    tasks.append({"status": "pending", "description": description})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
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
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task_to_complete = tasks[task_number - 1]
        if task_to_complete["status"] == "pending":
            task_to_complete["status"] = "completed"
            save_tasks(tasks)
            print(f"Completed task: {task_to_complete['description']}")
        else:
            print("Task is already completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task_to_delete = tasks[task_number - 1]
        tasks.remove(task_to_delete)
        save_tasks(tasks)
        print(f"Deleted task: {task_to_delete['description']}")
    else:
        print("Invalid task number.")

def main():
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