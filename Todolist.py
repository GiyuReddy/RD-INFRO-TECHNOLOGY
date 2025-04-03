tasks = []

def show_tasks():
    """Display the to-do list"""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    """Add a task to the list"""
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    """Remove a task from the list"""
    show_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def update_task():
    """Update a task in the list"""
    show_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    """Main function to run the to-do list app"""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
