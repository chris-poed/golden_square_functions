import pytest
from lib.todo_list import TodoList

def test_adds_a_task_to_the_task_list():
    task_list = TodoList()
    task_list.add_task('book a food delivery')
    assert task_list.task_list == ['book a food delivery']

def test_adds_multiple_tasks_to_the_task_list():
    task_list = TodoList()
    task_list.add_task('book a food delivery')
    task_list.add_task('take out the bins')
    task_list.add_task('book a holiday')
    assert task_list.task_list == ['book a food delivery', 'take out the bins', 'book a holiday']


def test_returns_the_list_of_tasks():
    task_list = TodoList()
    task_list.add_task('book a food delivery')
    task_list.add_task('take out the bins')
    task_list.add_task('book a holiday') 
    assert task_list.get_list() == ['book a food delivery', 'take out the bins', 'book a holiday']

def test_complete_task_deletes_task_from_the_list():
    task_list = TodoList()
    task_list.add_task('book a food delivery')
    task_list.add_task('take out the bins')
    task_list.add_task('book a holiday')
    task_list.complete_task('take out the bins')
    assert task_list.task_list == ['book a food delivery', 'book a holiday']