from django.test import TestCase
from .models import Task
# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(description="des 1")
        Task.objects.create(description="des 2", status=Task.DONE)

    def test_task_set_done(self):
        task1 = Task.objects.get(description="des 1")
        task2 = Task.objects.get(description="des 2")
        self.assertEqual(task1.setDone(), Task.DONE)
        self.assertEqual(task1.setDone(), "have done")
