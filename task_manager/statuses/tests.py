from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Status

User = get_user_model()


class StatusTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="test_user", password="testpass1"
        )
        self.status1 = Status.objects.create(name="In Progress")

    def test_create_status(self):
        self.client.force_login(self.user1)
        create_url = reverse("status_create")
        list_url = reverse("status_list")
        self.client.post(
            create_url,
            {"name": "Blocked"},
        )
        response = self.client.get(list_url)
        self.assertContains(response, "Blocked")

    def test_update_status(self):
        self.client.force_login(self.user1)
        update_url = reverse("status_update", kwargs={"pk": self.status1.pk})
        list_url = reverse("status_list")
        self.client.post(
            update_url,
            {"name": "Closed"},
        )
        self.status1.refresh_from_db()
        self.assertEqual(self.status1.name, "Closed")
        response = self.client.get(list_url)
        self.assertContains(response, "Closed")
        self.assertNotContains(response, "In Progress")

    def test_delete_status(self):
        self.client.force_login(self.user1)
        delete_url = reverse("status_delete", kwargs={"pk": self.status1.pk})
        list_url = reverse("status_list")
        self.client.post(delete_url)
        response = self.client.get(list_url)
        self.assertNotContains(response, "In Progress")
