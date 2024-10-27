import sys  # Import the sys module to access command-line arguments and system-specific parameters
import os  # Import the os module to interact with the operating system, including file and directory operations


# Specify the filename to store tasks
TASKS_FILE_PATH = "tasks.txt"

# Function to load tasks from the designated storage file
def retrieve_tasks():
    if not os.path.isfile(TASKS_FILE_PATH):
        return []  # Provide an empty list if the file is absent
    with open(TASKS_FILE_PATH, 'r') as task_file:
        return [task.strip() for task in task_file.readlines()]  # Read each line and remove any extra spaces


# Function to update the task storage file with the current task list
def update_task_file(tasks):
    with open(TASKS_FILE_PATH, 'w') as task_file:
        for task in tasks:
            task_file.write(f"{task}\n")  # Record each task on a separate line


# Function to add a new task with a given description
def add_task(task_description):
    current_tasks = retrieve_tasks()  # Retrieve the current list of tasks
    current_tasks.append(task_description)  # Add the new task to the list
    update_task_file(current_tasks)  # Store the updated list of tasks
    print(f"Task added: {task_description}")


# Function to display all tasks in a numbered list format
def list_tasks():
    tasks = retrieve_tasks()  # Get the list of tasks
    if not tasks:
        print("No tasks available.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")  # Print each task with its position number


# Marks a task as completed based on its position in the list
def complete_task(index):
    tasks = retrieve_tasks()  # Load the current list of tasks
    try:
        completed_task = tasks.pop(index - 1)  # Remove the task located at the specified index
        update_task_file(tasks)  # Save the revised task list to the file
        print(f"Task completed: {completed_task}")
    except IndexError:
        print("Error: Task number is invalid.")


# Deletes a task from the list by its position
def delete_task(index):
    tasks = retrieve_tasks()  # Load the current task list
    try:
        deleted_task = tasks.pop(index - 1)  # Remove the task at the specified position
        update_task_file(tasks)  # Save the modified task list
        print(f"Task deleted: {deleted_task}")
    except IndexError:
        print("Error: Task number provided is not valid.")


# Main function to manage command-line commands and arguments
def main():
    if len(sys.argv) < 2:  # Check if a command is given
        print("Usage: python task_manager.py [command] [arguments]")
        return  # Stop if no command is provided

    command = sys.argv[1]  # Extract the command from input arguments

    if command == "add" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])  # Combine arguments to form a task description
        add_task(description)  # Call function to add the new task
    elif command == "list":
        list_tasks()  # Call function to display all tasks
    elif command == "complete" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2])  # Convert input argument to an integer
            complete_task(index)  # Call function to mark the task as complete
        except ValueError:
            print("Error: Please provide a valid task number.")  # Handle invalid input
    elif command == "delete" and len(sys.argv) == 3:
        try:
            index = int(sys.argv[2])  # Convert input argument to an integer
            delete_task(index)  # Call function to delete the task
        except ValueError:
            print("Error: Please provide a valid task number.")  # Handle invalid input
    else:
        print("Invalid command. Available commands: add, list, complete, delete.")

# Execute main function only if script is run directly
if __name__ == "__main__":
    main()
