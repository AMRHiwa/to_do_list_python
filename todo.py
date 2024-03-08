# this program developed by Mohammad Rasoul Azizi
# Winter 2024
# to do list programm


# Import Libraries
import csv
import os
import sys



# Create class for Tasks with title, priority and done attributes
class Task:
    def __init__(self, title, priority='Medium', done=0):
        self.title = title
        self.priority = priority
        self.done = done


# Create TodoList class to manage the to do list program
class TodoList:
    def __init__(self):

        # variabe to save file and directory
        self.file_name = 'todo.csv'

        # tasks use for saving the tasks in one list as object from Task class
        self.tasks = list()

        # call the load_tasks method for load tasks from file to program
        self.load_tasks()


    # define load_tasks method for load tasks from file to program
    def load_tasks(self):

        # Checking the existence of the file in the specified path
        if os.path.exists(self.file_name):

            # open csv file as csvfile
            with open(self.file_name) as csvfile:

                # read all information from file and save in file_read variable
                file_read = csv.reader(csvfile)

                # Browse stored information row by row
                for row in file_read:

                    # Checking the length of stored information
                    if len(row) == 3:

                        # adding the stored tasks in csvfile as Task's object in tasks variable
                        self.tasks.append(Task(row[0], row[1], row[2]))

    # define the save_tasks for saving tasks from tasks variable into csv file
    def save_tasks(self):

        # opening the csv file as csvfile
        with open(self.file_name, 'w', newline='') as csvfile:

            # create the writer object for writing into csv file
            writer = csv.writer(csvfile)

            # Browse stored tasks in tasks variable row by row
            for row in self.tasks:

                # write each task in file row by row
                writer.writerow([row.title, row.priority, row.done])

    # define the create_task for create a new task and save it into csv file
    def create_task(self, title, priority='Medium', done=0):

        # adding a new Task's object with given parameter into task's variable
        self.tasks.append(Task(title, priority, done))

        # call the save_tasks method for save new task into csv file
        self.save_tasks()

        # showing the successfully message for creating task.
        print(f'Task \"{title}\" created successfully.')


    # define List_tasks for showing the stored tasks in a table
    def list_tasks(self):

        # Checking the presence of at least one task in the tasks variable.
        if self.tasks:

            # showing the task as below form
            print('Task List:')
            print("{:<6} {:<15} {:<10} {:<10}".format('Index', "Title", "Priority", "Done"))
            index = 1
            for  row in self.tasks:
                print("{:<6} {:<15} {:<10} {:<10}".format(index, str(row.title), str(row.priority), str(row.done)))
                index += 1
        
        # if there is no any task in tasks variable
        else:

            # showing below message.
            print("No tasks found.")


    # define update_task for update and change the stored tasks
    def update_task(self, title, field, edit):

        # open csv file as csvfile
        with open(self.file_name) as file:

            # read all information in csvfile as list
            read = list(csv.reader(file))

        # define the flag for checking the specific task is exist or not
        flag = False

        # brow the tasks row by row
        for row in read:

            # Checking whether the title of the row is the same as the given title.
            if title == row[0]:

                # give the True value to flag for existing the title
                flag = True

                # checking the is field done
                if field == 'done':

                    # setting new value
                    row[2] = edit

                # checking the is field priority
                elif field == 'priority':

                    # setting new value
                    row[1] = edit
        
        # if title is exist in tasks
        if flag:

            # opening csv file as file
            with open(self.file_name, 'w', newline='') as file:
                
                # create the writer object for writing values into file
                writer = csv.writer(file)

                # write the updated tasks into file
                writer.writerows(read)
            
            # showing the successfull update message
            print(f'Task "{title}" updated successfully.')

        else:

            # if there is no such this title showing the "Invalid title" message
            print('Invalid title.')


    # define the delete_task method for deleting the specific task from stored tasks
    def delete_task(self, title):

        # open the csv file as file
        with open(self.file_name) as file:

            # reading all information from file
            read = list(csv.reader(file))

        # copying the information into temporary variable
        temp = read.copy()

        # define the flag for checking the specific task is exist or not
        flag = False

        # brow the tasks row by row
        for row in temp:

            # Checking whether the title of the row is the same as the given title.
            if title == row[0]:
            
                # give the True value to flag for existing the title
                flag = True

                # remove the task from stored task
                read.remove(row)
        
        # if title is exist in tasks
        if flag:

            # open csv file as file
            with open(self.file_name, 'w', newline='') as file:
                
                # create writer object for writing values into file
                writer = csv.writer(file)

                # write updated tasks into the file
                writer.writerows(read)

            # showing the deleted successfull message
            print(f'Task "{title}" deleted successfully.')

        # if there is no such this title 
        else:

            # showing Invalid title.
            print('Invalid title.')
            
    # define the clear_list method for clearing the tasks
    def clear_list(self):

        # create a empty list
        empty_list = list()

        # open csv file as file
        with open(self.file_name, 'w', newline='') as file:
            
            # create a writer object for writing values into file
            writter = csv.writer(file)

            # writing the empty list into the file
            writter.writerows(empty_list)

            # showing the message for user
            print('To-do list cleared successfully.')

    # defining the get_task method for showing a specific task
    def get_task(self, title):

        # open csv file as file
        with open(self.file_name) as file:

            # reading all information from file and save them in read variable
            read = list(csv.reader(file))

        # brow the tasks row by row
        for row in read:

            # Checking whether the title of the row is the same as the given title.
            if title == row[0]:

                # showing the task as specific form for user
                print("{:<15} {:<10} {:<10}".format('Title', 'Priority', 'Done'))
                print("{:<15} {:<10} {:<10}".format(row[0], row[1], row[2]))

# defining the main function
def main():

    # create a object from TodoList class
    obj = TodoList()

    # getting the arguments that user writes them in terminal
    arg_pars_command = sys.argv

    # Checking the first word that the user wrote in the terminal commands, is the word "create"?
    if arg_pars_command[1] == 'create':

        # Checking whether the length of the command entered by the user in the terminal is equal to 5 or not?
        if len(arg_pars_command) == 5:

            # call create_task method with title, priority, done arguments
            obj.create_task(arg_pars_command[2], arg_pars_command[3], arg_pars_command[4])

        # Checking whether the length of the command entered by the user in the terminal is equal to 4 or not?
        elif len(arg_pars_command) == 4:

            # call create_task method with title, priority arguments
            obj.create_task(arg_pars_command[2], arg_pars_command[3])

        else:

            # call create_task method with title argument
            obj.create_task(arg_pars_command[2])
    
    # Checking the first word that the user wrote in the terminal commands, is the word "update"?
    elif arg_pars_command[1] == 'update':

        # calling update_task with title, field, new_value arguments
        obj.update_task(arg_pars_command[2], arg_pars_command[3], arg_pars_command[4])

    # Checking the first word that the user wrote in the terminal commands, is the word "delete"?
    elif arg_pars_command[1] == 'delete':

        # calling delete_task with title argument
        obj.delete_task(arg_pars_command[2])
    
    # Checking the first word that the user wrote in the terminal commands, is the word "create"?
    elif arg_pars_command[1] == 'clear':

        # calling the clear_list method
        obj.clear_list()

    # Checking the first word that the user wrote in the terminal commands, is the word "search"?
    elif arg_pars_command[1] == 'search':

        # calling get_task with title argument
        obj.get_task(arg_pars_command[2])

    # Checking the first word that the user wrote in the terminal commands, is the word "list"?
    elif arg_pars_command[1] == 'list':

        # calling the list method
        obj.list_tasks()    

    # If the entered word is none of the above words:
    else:

        # showing the "Invalid Command." message.
        print("Invalid command.")

# Checking whether the main file is executed?
if __name__ == "__main__":

    # calling the main function
    main()
