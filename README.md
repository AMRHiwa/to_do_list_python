# To Do List Project
In the "To Do List" program, it has been tried to be implemented in Python and this program is a program that can be implemented in the terminal environment or the command prompt environment.

"To-do list" is a program for managing the list of tasks that we need to do, which gives us the ability to put our tasks in our list by title, necessity, completion, and this list can be updated. and added, reduced or changed its items.

This guide is prepared for you in two parts:
* <a href='#guide'>Program guide.</a>
* <a href=''>explains the structure of the program.</a>

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
In this section, you can delete all Items and Clear the to do list. Just enter the following command in the command prompt environment:

> `python todo.py clear`

<h4 id='search'>Search Item</h4>
In this section, you can search the items by them names. Just enter the following command in the command prompt environment:

> `python todo.py search title`
