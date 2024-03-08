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

            # check identity title of row with given title
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

            # if there is no such this title showing the Invalid title. message
            print('Invalid title.')



    def delete_task(self, title):
        with open(self.file_name) as file:
            read = list(csv.reader(file))
        temp = read.copy()
        flag = False
        for row in temp:
            if title == row[0]:
                flag = True
                read.remove(row)
        if flag:
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(read)
            print(f'Task "{title}" deleted successfully.')
        else:
            print('Invalid title.')
            
    def clear_list(self):
        empty_list = list()
        with open(self.file_name, 'w', newline='') as file:
            writter = csv.writer(file)
            writter.writerows(empty_list)
            print('To-do list cleared successfully.')

    def get_task(self, title):
        with open(self.file_name) as file:
            read = list(csv.reader(file))
        flag = False
        for row in read:
            if title == row[0]:
                flag = True
                print("{:<15} {:<10} {:<10}".format('Title', 'Priority', 'Done'))
                print("{:<15} {:<10} {:<10}".format(row[0], row[1], row[2]))
        # if flag:
        #     print()
def main():
    obj = TodoList()
    arg_pars_command = sys.argv
    if arg_pars_command[1] == 'create':
        if len(arg_pars_command) == 5:
            obj.create_task(arg_pars_command[2], arg_pars_command[3], arg_pars_command[4])
        elif len(arg_pars_command) == 4:
            obj.create_task(arg_pars_command[2], arg_pars_command[3])
        else:
            obj.create_task(arg_pars_command[2])
    
    elif arg_pars_command[1] == 'update':
        obj.update_task(arg_pars_command[2], arg_pars_command[3], arg_pars_command[4])
                
    elif arg_pars_command[1] == 'delete':
        obj.delete_task(arg_pars_command[2])
    
    elif arg_pars_command[1] == 'clear':
        obj.clear_list()

    elif arg_pars_command[1] == 'search':
        obj.get_task(arg_pars_command[2])

    elif arg_pars_command[1] == 'list':
        obj.list_tasks()    

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
