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

    def create_task(self, title, priority='Medium', done=0):
        self.tasks.append(Task(title, priority, done))
        self.save_tasks()
        print(f'Task \"{title}\" created successfully.')

    def list_tasks(self):
        if self.tasks:
            print('Task List:')
            print("{:<6} {:<15} {:<10} {:<10}".format('Index', "Title", "Priority", "Done"))
            index = 1
            for  row in self.tasks:
                print("{:<6} {:<15} {:<10} {:<10}".format(index, str(row.title), str(row.priority), str(row.done)))
                index += 1
        else:
            print("No tasks found.")


    def update_task(self, title, field, edit):
        with open(self.file_name) as file:
            read = list(csv.reader(file))
        flag = False
        for row in read:
            if title == row[0]:
                flag = True
                if field == 'done':
                    row[2] = edit
                elif field == 'priority':
                    row[1] = edit
        if flag:
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(read)
            print(f'Task "{title}" updated successfully.')
        else:
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
