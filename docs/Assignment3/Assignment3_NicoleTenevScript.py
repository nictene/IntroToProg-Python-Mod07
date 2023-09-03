#.....................................#
# Title: Home Inventory Python Script
# Desc: A script that helps you create a to do list
# Change Log: (Who, When, What)
# NTenev,  08-015-2023, Created File
#....................................#

# Function to save the ToDo list to the file
def save_todo_list(todo_list):
    # Open the file in write mode and save each task with its priority
    with open("ToDo.txt", "w") as file:
        for row in todo_list:
            file.write(f"Task: {row['Task']}, Priority: {row['Priority']}\n")

# Function to load the ToDo list from the file
def load_todo_list():
    todo_list = []
    try:
        # Try to open the file in read mode and load tasks and priorities
        with open("ToDo.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    task, priority = line.strip().split(", ")
                    todo_list.append({"Task": task.split(": ")[1], "Priority": priority.split(": ")[1]})
    except FileNotFoundError:
        pass
    return todo_list

# Function to add a task to the ToDo list
def add_task(todo_list):
    task_name = input("Enter the name of the task: ")
    task_priority = input("Enter the priority of the task: ")

    # Add the new task as a dictionary to the todo_list
    todo_list.append({"Task": task_name, "Priority": task_priority})
    print("Task added successfully!")

# Function to display all tasks in the ToDo list
def display_tasks(todo_list):
    if not todo_list:
        print("No tasks found.")
    else:
        for task in todo_list:
            print(f"Task: {task['Task']}, Priority: {task['Priority']}")

# Function to delete a task from the ToDo list
def delete_task(todo_list):
    task_to_delete = input("Enter the name of the task to delete: ")
    deleted = False
    for task in todo_list.copy():
        if task['Task'] == task_to_delete:
            todo_list.remove(task)
            deleted = True

    if deleted:
        print(f"{task_to_delete} has been deleted.")
    else:
        print(f"{task_to_delete} not found.")

# Main function to run the program
def main():
    # Load existing tasks from the file or initialize an empty list
    todo_list = load_todo_list()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            display_tasks(todo_list)
        elif choice == "3":
            delete_task(todo_list)
        elif choice == "4":
            save_todo_list(todo_list)
            print("ToDo list saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

# Call the main function to start the program
main()
