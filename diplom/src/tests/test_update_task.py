import pytest
# not working
from views import UpdateView
from unittest import TestCase


class TestUpdatingTask(TestCase):
    def test_update_task(self):
        """Тест обновления существующей задачи"""
        data = {
            "title": "write some code",
            "description": "second task",
            "completed": 1
        }
        url = 'http://locahost:8000/task-create/'
        response = "success"
