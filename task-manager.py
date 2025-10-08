tasks = []

def display_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("===============================")

def add_task():
    task = input("Enter the task description: ")
    tasks.append({"title": task, "completed": False})
    print(f'Task "{task}" added.')

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx + 1}. [{status}] {task['title']}")

    print("===============================")

def complete_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number.")
            return
        
        tasks_to_complete = tasks[task_num - 1]
        tasks_to_complete["completed"] = True
        print(f'Task "{tasks_to_complete["title"]}" marked as completed.')
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    view_tasks()

    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the task number to remove: "))
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number.")
            return
        
        removed_task = tasks.pop(task_num - 1)
        print(f'Task "{removed_task["title"]}" removed.')
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()