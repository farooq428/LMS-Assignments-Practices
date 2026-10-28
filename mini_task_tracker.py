
import json

FILE_NAME = "tasks.json"


# Load saved tasks from the JSON file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

            if not isinstance(tasks, list):
                print("Invalid task file. Starting with an empty list.")
                return []

            return tasks

    except FileNotFoundError:
        print("No saved tasks found. Starting a new task list.")
        return []

    except (json.JSONDecodeError, UnicodeDecodeError):
        print("The task file is invalid. Starting with an empty list.")
        return []


# Save tasks to the JSON file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task():
    title = input("Task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added successfully!")


# Display all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- YOUR TASKS ---")

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


# Mark a task as completed
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[number - 1]

        if task["done"]:
            print("This task is already completed.")
        else:
            task["done"] = True
            save_tasks()
            print("Task completed successfully!")

    except ValueError:
        print("Please enter a valid whole number.")


# Delete a task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)
        save_tasks()
        print(f"Deleted task: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid whole number.")


# Load existing tasks when the program starts
tasks = load_tasks()


# Main menu
while True:
    print("\n--- TASK TRACKER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Task Tracker!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
