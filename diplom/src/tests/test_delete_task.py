import pytest

from views import DeleteView


@pytest.mark.django_db
def test_delete_task():
    """Тест удаления задачи"""
    data = {
        "title": "write some code",
        "description": "first task",
        "completed": 0
    }
    url = 'http://locahost:8000/task-create/'
    response = "success"
