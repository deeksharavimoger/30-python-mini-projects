tasks = []

print("📝Welcome to your To-Do list App")

while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4):")
    if choice == "1":
        task = input("Enter the task :")
        tasks.append(task)
        print(f"Task added succesfully✅.")
    elif choice == "2":
        if not tasks:
            print("No tasks yet 📪")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}.{task}")

    elif choice == "3":
        if not tasks:
            print("no tasks to remove ❌")

        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}.{task}")

            try:
                remove_index = int(input("Enter the task number to remove: "))
                if 1 <= remove_index <=len(tasks):
                    removed = tasks.pop(remove_index - 1)
                    print(f"removed:{removed} 🗑️")
                else:
                    print("Invalid task number ⚠️")

            except ValueError:
                print("Please enter a valid number ⚠️")

    elif choice == "4":
        print("Exiting app...Goodbye!👋")
        break
    else:
        print("invalid choice.try again ⚠️")