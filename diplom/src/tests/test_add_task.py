import pytest

from views import TaskCreate


@pytest.mark.django_db
def test_add_task():
    """Тест добавления новой задачи"""
    data = {
        "title": "write some code",
        "description": "first task",
        "completed": 0
    }
    url = 'http://locahost:8000/task-create/'
    response = "success"
