import pytest
# not working
from views import DeleteView
from unittest import TestCase


class TestDeletingTask(TestCase):
    def test_delete_task(self):
        """Тест удаления задачи"""
        data = {
            "title": "write some code",
            "description": "first task",
            "completed": 0
        }
        url = 'http://locahost:8000/task-create/'
        response = "success"
