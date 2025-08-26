import  sys

def menu():
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit\n")
    choice = input("Enter your choice (1-4): ")
    return choice

def add_task():
    with open("todo_list.txt", "a") as file:
        new_task = input("Enter the task you want to add:\n")
        file.write(new_task + "\n")
    print(f'Task "{new_task}" added.\n')

def view_tasks():
    try:
        print("Your Current Tasks:")
        with open("todo_list.txt") as file:
            x=1
            for tasks in file:
                print(f"{str(x)}. {tasks}")
                x+=1
                           
    except FileNotFoundError:
        print("No tasks available. \n")

def remove_tasks():
    rem_no=int(input("Enter the task number you want to remove: "))
    try:
        content=[]
        with open("todo_list.txt") as file:
            for tasks in file:
                    content.append(tasks)
            content.pop(rem_no-1)
        with open("todo_list.txt","w") as file:
            for updated_task in content:    
                file.write(updated_task)
        print(f"Task no. {rem_no} removed.")
    except Exception as e:
        print(e)
      
def quit():
    view_tasks()
    print("Exiting the Program. Goodbye!")
    sys.exit("User exited the program")

while True:
    choice=menu()
    match choice:
        case "1":
            add_task()
        case "2":
            view_tasks()
        case "3":
            remove_tasks()
        case "4":
            quit()
        case _:
            print("Invalid Choice.")
            quit()


