# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def display_menu():
    """
    Displays the main menu to the user.
    """
    print("\n============================")
    print("       TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

def add_task(tasks):
    """
    Prompts the user to enter a new task and appends it to the list.
    """
    task_desc = input("Enter task: ")
    tasks.append(task_desc)
    print(f'Task added: "{task_desc}"')

def view_tasks(tasks):
    """
    Displays all current tasks with their corresponding numbers.
    """
    if not tasks:
        print("Your to-do list is currently empty.")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(tasks):
    """
    Displays tasks, prompts the user for a task number, and removes it.
    """
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return
        
    # Show the current list first so the user knows the numbers
    view_tasks(tasks)
    
    try:
        task_num = int(input("Enter task number to delete: "))
        
        # Check if the number is within the valid range (1 to length of list)
        if 1 <= task_num <= len(tasks):
            # pop() takes the index, which is task_num - 1
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    """
    Main loop that drives the To-Do List program.
    """
    # The master list storing all tasks
    tasks = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        print() # Add an empty line for cleaner output spacing
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()