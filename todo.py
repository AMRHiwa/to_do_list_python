# this program developed by Mohammad Rasoul Azizi
# Winter 2024
# to do list programm



import csv
import os
import sys


class Task:
    def __init__(self, title, priority='Medium', done=0):
        self.title = title
        self.priority = priority
        self.done = done


class TodoList:
    def __init__(self):
        self.file_name = 'todo.csv'
        self.tasks = list()
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name) as csvfile:
                file_read = csv.reader(csvfile)
                for row in file_read:
                    # print(row)
                    if len(row) == 3:
                        self.tasks.append(Task(row[0], row[1], row[2]))

    def save_tasks(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.tasks:
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
