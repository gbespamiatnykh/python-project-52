from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Status

User = get_user_model()


class StatusTest(TestCase):
    fixtures = ["statuses.json", "users.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user1.set_password("testpass1")
        self.user1.save()
        self.status1 = Status.objects.get(pk=1)

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
            {"name": "Testing"},
        )
        self.status1.refresh_from_db()
        self.assertEqual(self.status1.name, "Testing")
        response = self.client.get(list_url)
        self.assertContains(response, "Testing")
        self.assertNotContains(response, "In Progress")

    def test_delete_status(self):
        self.client.force_login(self.user1)
        delete_url = reverse("status_delete", kwargs={"pk": self.status1.pk})
        list_url = reverse("status_list")
        self.client.post(delete_url)
        response = self.client.get(list_url)
        self.assertNotContains(response, "In Progress")
