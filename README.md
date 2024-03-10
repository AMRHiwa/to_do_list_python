# To Do List Project
In the "To Do List" program, it has been tried to be implemented in Python and this program is a program that can be implemented in the terminal environment or the command prompt environment.

"To-do list" is a program for managing the list of tasks that we need to do, which gives us the ability to put our tasks in our list by title, necessity, completion, and this list can be updated. and added, reduced or changed its items.

This guide is prepared for you in two parts:
* <a href='#guide'>Program guide.</a>
* <a href='#structure'>explains the structure of the program.</a>

<h3 id='guide'> Program guide :</h3>
This program is developed for command prompt and terminal environment. To use this program, just download the source code file and save it in your computer memory.

The tools of this program are as follows:

* <a href='#add'>Add Item</a>
* <a href='#delete'>Delete Item</a>
* <a href='#list'>Show list</a>
* <a href='#update'>Update Item</a>
* <a href='#clear'>Clear Items</a>
* <a href='#search'>Search Item</a>


<h4 id='add'>Add Item</h4>
In this section, you can add new items to the program. Just enter the following command in the command prompt environment:

> `python todo.py create title priority done`

if you don't give it the priority and done of your work, the program set medium and 0 as default for them.

<h4 id='delete'>Delete Item</h4>
In this section, you can delete the items by them names. Just enter the following command in the command prompt environment:

> `python todo.py delete title`

If there is an item with such a title, it will be removed from the list.

<h4 id='list'>Show List</h4>
In this section, you can watch your To-Do list. Just enter the following command in the command prompt environment:

> `python todo.py list`

If you enter this command, you will see a structure 

like this: 


|Task List:|    |   |   |
| --- | --- | --- | --- |
|Index  |Title  |Priority|  Done |      
| 1 | Task 1 | Low | 1 |
|2 | Task 2 | Medium | 0 |

<h4 id='update'>Update Item</h4>
In this section, you can edit your To-Do list priority or Done feature of your Item by its title. Just enter the following command in the command prompt environment:

> `python todo.py update title priority new-value`

or

> `python todo.py update title Done new-value`


<h4 id='clear'>Clear Items</h4>
In this section, you can delete all items. Just enter the following command in the command prompt environment:

> `python todo.py clear`

<h4 id='search'>Search Item</h4>
In this section, you can Search the items by them names. Just enter the following command in the command prompt environment:

> `python todo.py search title`

---
---

<h3 id='structure'> Structure of program :</h3>

This program is implemented by two classes and a function, whose features are mentioned below:

+ <a href='#task_class'>Class Task</a>
+ <a href='#todolist_class'>Class TodoList</a>
+ <a href='#task_class'>main Function</a>

<h4 id='task_class'>Class Task:</h4>
Using an initial function, this class considers and creates an object with the attributes title, priority, and done for better management of tasks.

<h4 id='todolist_class'>TodoList Task:</h4>
This class is used to manage "tasks" in the program and the following methods are defined and implemented to implement this management:

+ <a href="#init">init</a>
+ <a href="#load_tasks">load_tasks</a>
+ <a href="#save_tasks">save_tasks</a>
+ <a href="#create_tasks">create_task</a>
+ <a href="#list_tasks">list_tasks</a>
+ <a href="#update_task">update_task</a>
+ <a href="#delete_task">delete_task</a>
+ <a href="#clear_list">clear_list</a>
+ <a href="#get_task">get_task</a>

<h5 id='init'>init:</h5>

In this method, we store the "path to save the file" in a variable called file_name, consider an empty list to store tasks in the tasks variable, and then call the load_tasks method to retrieve the information from the data file.

<h5 id='load_tasks'>load_tasks:</h5>

In this method, it reads the information stored in the data file and then stores it as a series of objects from the task class in the tasks variable.

<h5 id='save_tasks'>save_tasks:</h5>

In this method, the information stored in the task variable is read, and then the former information is placed in the data file in a special format.

<h5 id='create_tasks'>create_tasks:</h5>

In this method, a new object of the task class is created by getting the information of the task title, task priority, and task completion status and saves it in the tasks variable.

<h5 id='list_tasks'>list_tasks:</h5>

This method first reads the data file and then displays all the saved tasks as a table in the output.

<h5 id='update_task'>update_task:</h5>

This method uses the title that the user enters in the list of tasks and updates the desired task based on priority or completion status and saves it again in the data file.


<h5 id='delete_task'>delete_task:</h5>

This method first takes a title among the tasks, and if it finds the desired task, it deletes it and then re-places the remaining tasks in the data file.

<h5 id='clear_list'>clear_list:</h5>

This method deletes all the tasks stored in the data file.

<h5 id='get_task'>get_task:</h5>

By taking the title of a task, this method finds it in the list of tasks stored in the data file and displays it to the user if it exists.