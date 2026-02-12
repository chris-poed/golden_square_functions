# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDoList:

    def __init__(self):
        def self.task_list = [] # task_list will be a list with each item being a task
        pass # No code here yet

    def add_task(self, task):
        # adds a task to the task_list
        # param is a string for the task, e.g. 'book a food delivery'
        # Returns nothing
        # Side effects: 
        # adds a task to the task_list, e.g. task_list.append['book a food delivery']
        # prints a message to the user 'Task is added'
    
    def list_tasks(self):
        # lists all the current tasks in the task_list
        # returns the list to the user

    def complete_task(self, task):
        # removes a task from the list
        # param is a string matching an existing task, e.g. 'book a food delivery'
        # if the task exists, remove it from the list and print the current task list to the user
        # if the task does not exist, print a message to the user 'The requested task is not found, please enter a task again'
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a task
Add the task to the task_list
"""
task_list = TodoList()
task_list.add_task('book a food delivery')

"""
Given multiple tasks
Adds multiple tasks to the list
"""
task_list = TodoList()
task_list.add_task('book a food delivery')
task_list.add_task('take out the bins')
task_list.add_task('book a holiday')

"""
Lists the tasks in the task_list
"""
task_list = TodoList()
task_list.add_task('book a food delivery')
task_list.add_task('take out the bins')
task_list.add_task('book a holiday')
task_list.get_list()

"""
Given a task string
Deletes the task from the list
"""
task_list = TodoList()
task_list.add_task('book a food delivery')
task_list.add_task('take out the bins')
task_list.add_task('book a holiday')
task_list.complete_task('take out the bins')


# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
