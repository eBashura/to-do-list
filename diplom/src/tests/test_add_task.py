import pytest
# not working
from views import TaskCreate
from unittest import TestCase


class TestAddingTask(TestCase):
    def test_add_task(self):
        """Тест добавления новой задачи"""
        data = {
            "title": "write some code",
            "description": "first task",
            "completed": 0
        }
        url = 'http://locahost:8000/task-create/'
        response = "success"
