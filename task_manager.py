import csv
import os

def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. View Tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append([task, 'Pending'])

def mark_task_done(tasks):
    task = input("Enter task to mark as done: ")
    for t in tasks:
        if t[0] == task:
            t[1] = 'Done'
            break
    else:
        print("Task not found.")

def view_tasks(tasks):
    for task, status in tasks:
        print(f"{task} [{status}]")

def save_tasks(tasks):
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

def load_tasks():
    if not os.path.exists('tasks.csv'):
        return []
    with open('tasks.csv', 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_task_done(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
    

