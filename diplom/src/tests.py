from django.test import TestCase
from models import Task
from django.contrib.auth.models import User
from django.urls import reverse


class TaskTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='test_1', password='useruser')
        self.client.login(username='test_1', password='useruser')

    def test_task_create_view(self):
        # Create test task
        response = self.client.post(reverse('task_create'), {'title': 'New Task'})
        self.assertEqual(response.status_code, 302) 

    def test_task_update_view(self):
        # Test task update
        task = Task.objects.create(user=self.user, title='Test Task', description='Description', completed=False)
        response = self.client.post(reverse('task_update', args=[task.pk]), {'title': 'Updated Task'})
        self.assertEqual(response.status_code, 302)  

    def test_task_delete_view(self):
        # Test task delete
        task = Task.objects.create(user=self.user, title='Test Task', description='Description', completed=False)
        response = self.client.post(reverse('task_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
