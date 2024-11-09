#define a main function that contain todo lidt program logic
def main():
    #initialize an empty lists to store tasks
    tasks = []
    #startan infinite loop to keep the program running until user chooses to  exit 
    while True:
        #print the menu options 
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        #prompt the user to enter the choice and store it in choice variable 

        choice = input("Enter your choice: ")
        #check if the user choose option 1 to add a new task 

        if choice == '1':
            print()#print a blank line for formatting 
            #prompt the user no.of tasks they want to add 
            n_tasks = int(input("How may task you want to add: "))
            #use a loop to add specified numberof tasks
            for i in range(n_tasks):
                #ask the user to enter the task description
                task = input("Enter the task: ")
                #add the task to a dictionary with a "done" status  set  to false
                tasks.append({"task": task, "done": False})
                #confirm that the task has been added
                print("Task added!")
         #check if the user choose option 2  to show the list of tasks        
        elif choice == '2':
            #print a header for the tasklist
            print("\nTasks:")
            #loop through each task ,displaying itsindex,description and status
            for index, task in enumerate(tasks):
                #set the statusmwhether the task is marked as done 
                status = "Done" if task["done"] else "Not Done"
                #print the task with its nnumber,description,and sstatus
                print(f"{index + 1}. {task['task']} - {status}")
         #check if the user chooses 3 option to mark tasks as done         
        elif choice == '3':
            #prompt the user for the to mark as done and adjust for 0-based indexing
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            #check if the entered choice is within the range of tasks 
            if 0 <= task_index < len(tasks):
                #mark the tasks as done by setting "done to true"
                tasks[task_index]["done"] = True
                #confirm that the task has been marked as done 
                print("Task marked as done!")
            else:
                #print an error if the entered number isinvalid 
                print("Invalid task number.")
         #check if tke user chooses option 4 to exit the program       
        elif choice == '4':
            #print a message to exit a program
            print("Exiting the To-Do List.")
            #break the loop to end a program
            break
        #handle any invalid input from the user 
        else:
            #print an error message if the choice is not one of the options 
            print("Invalid choice. Please try again.")
#check if this script is being run directly
if __name__ == "__main__":
    #call main function to start the program
    main()
