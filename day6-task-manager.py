def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ] " + task)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[✔]")
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        print("\n=== Mini Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()