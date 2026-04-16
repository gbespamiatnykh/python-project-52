from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Task

User = get_user_model()


class TaskTest(TestCase):
    fixtures = ["labels.json", "users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user1.set_password("testpass1")
        self.user1.save()
        self.task1 = Task.objects.get(pk=1)

    def test_create_task(self):
        self.client.force_login(self.user1)
        create_url = reverse("task_create")
        self.client.post(
            create_url,
            {
                "name": "Refactore application structure",
                "description": "Clean up code.",
                "status": 3,
                "executor": 2,
                "labels": [2, 3],
            },
        )
        task = Task.objects.get(name="Refactore application structure")
        show_url = reverse("task_show", kwargs={"pk": task.pk})
        response = self.client.get(show_url)
        self.assertContains(response, "Refactore application structure")
        self.assertContains(response, "Clean up code.")
        self.assertContains(response, "To Do")
        self.assertContains(response, "Samuel Winchester")
        self.assertContains(response, "Review")

    def test_update_task(self):
        self.client.force_login(self.user1)
        update_url = reverse("task_update", kwargs={"pk": self.task1.pk})
        show_url = reverse("task_show", kwargs={"pk": self.task1.pk})
        self.client.post(
            update_url,
            {
                "name": "Optimize system perfomance",
                "description": self.task1.description,
                "status": 2,
                "executor": self.task1.executor.pk,
                "labels": [label.pk for label in self.task1.labels.all()],
            },
        )
        self.task1.refresh_from_db()
        show_url = reverse("task_show", kwargs={"pk": self.task1.pk})
        self.assertEqual(self.task1.name, "Optimize system perfomance")
        self.assertEqual(self.task1.status.name, "Closed")
        response = self.client.get(show_url)
        self.assertContains(response, "Optimize system perfomance")
        self.assertNotContains(response, "Perform improvments")
        self.assertContains(response, "Closed")
        self.assertNotContains(response, "In Progress")

    def test_delete_task(self):
        self.client.force_login(self.user1)
        delete_url = reverse("task_delete", kwargs={"pk": self.task1.pk})
        list_url = reverse("task_list")
        self.client.post(delete_url)
        response = self.client.get(list_url)
        self.assertNotContains(response, "Perform improvments")
