import sys

print("To-DO List")

task =[]

def menu():
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit\n")
    choice = input("Enter your choice (1-4): ")
    return choice
    

def add_task():
    new_task=input("Enter the task you want to add:\n ")
    task.append(new_task)
    print(f'Task "{new_task}" added.\n')

def view_tasks():
    if task != []:
        print("Your Current Tasks:")
        [print(f"{str(x+1)}. {task[x]} \n") for x in range(len(task))]
    else:
        print("No tasks available. \n")
        
def remove_task():
    view_tasks()
    rem_no=int(input("Enter the task number you want to remove: "))
    try:
        print(f"Task removed. \n")
        task.pop(rem_no-1)
    
    except IndexError:
        print("Invalid task number. \n")
    except Exception as e:
        print(f"An error occurred: {e} \n")

def quit():
    view_tasks()
    print("Exiting the program. Goodbye!")
    sys.exit("User exited the program.")

while True:
    choice=menu()
    match choice:
        case '1':
            add_task()
        case '2':
            view_tasks()
        case '3':
            remove_task()
        case '4':
            quit()
        case _:
            print("Invalid choice. Please enter a number between 1 and 4. \n")

# Simple To-Do List Application   

