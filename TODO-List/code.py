import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from tasks.txt, or return an empty list if file doesn't exist."""
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading tasks file: {e}")
        return []

def save_tasks(tasks):
    """Save all tasks to tasks.txt."""
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def show_tasks(tasks):
    """Display all current tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [1] View Tasks  [2] Add Task  [3] Delete Task  [4] Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()