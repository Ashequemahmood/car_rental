import datetime

def show_menu():
    print("\nTo-Do List Manager")
    print("1) Add a task")
    print("2) View tasks")
    print("3) Remove a task")
    print("4) Save tasks to file")
    print("5) Load tasks from file")
    print("6) Exit")
    choice = input("Enter your choice (1-6):\n")
    return choice


def add_task(tasks):
    task_name = input("Enter task name:\n")
    due_date_str = input("Enter the due date (YYYY-MM-DD):\n")
    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    tasks.append({"name": task_name, "due_date": due_date})
    
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        index = 1
        for task in tasks:
            print(f"{index}. {task['name']} - Due: {task['due_date']}")
            index += 1 
    
def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to remove:\n"))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Removed task: {removed_task['name']}")
    else:
        print("Invalid task number.")
        
def save_tasks(tasks, filename="tasks.txt"):
    file = open(filename, "w")
    for task in tasks:
        file.write(f"{task['name']},{task['due_date']}\n")
    file.close()
    print("Tasks saved to file.")
    
def load_tasks(filename="tasks.txt"):
    tasks = []
    file = open(filename, "r")
    for line in file:
        name, due_date_str = line.strip().split(",")
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        tasks.append({"name": name, "due_date": due_date})
    file.close()
    print("Tasks loaded from file.")
    return tasks
    
def main():
    tasks = []
    while(True):
        choice = show_menu()
        if(choice == "1"):
            add_task(tasks)
        elif(choice == "2"):
            view_tasks(tasks)
        elif(choice == "3"):
            remove_task(tasks)
        elif(choice == "4"):
            save_tasks(tasks)
        elif(choice == "5"):
            tasks = load_tasks()
        elif(choice == "6"):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    
main()