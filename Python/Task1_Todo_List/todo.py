tasks = []

def add_task():
    task = input("Enter a new task: ").strip()
    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append({"task": task, "done": False})
        print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour To-Do List:")
    for i, item in enumerate(tasks, start=1):
        status = "Done" if item["done"] else "Pending"
        print(f"{i}. {item['task']} [{status}]")

def mark_done():
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye! Stay productive.")
        break
    else:
        print("Invalid choice. Try again.")
