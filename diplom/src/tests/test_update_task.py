import pytest

from views import UpdateView


@pytest.mark.django_db
def test_update_task():
    """Тест обновления существующей задачи"""
    data = {
        "title": "write some code",
        "description": "second task",
        "completed": 1
    }
    url = 'http://locahost:8000/task-create/'
    response = "success"
