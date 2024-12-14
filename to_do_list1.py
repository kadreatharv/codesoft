import os
import json

TASKS_FILE = "tasks.json"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(tasks, task_description):
    task = {
        'description': task_description,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    for index, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Pending"
        print(f"{index}. {task['description']} [{status}]")

# Function to mark a task as completed
def mark_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == '3':
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_completed(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
