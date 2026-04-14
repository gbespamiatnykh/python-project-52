from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Label

User = get_user_model()


class LabelTest(TestCase):
    fixtures = ["labels.json", "users.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user1.set_password("testpass1")
        self.user1.save()
        self.label1 = Label.objects.get(pk=1)

    def test_create_label(self):
        self.client.force_login(self.user1)
        create_url = reverse("label_create")
        list_url = reverse("label_list")
        self.client.post(
            create_url,
            {"name": "High"},
        )
        response = self.client.get(list_url)
        self.assertContains(response, "High")

    def test_update_label(self):
        self.client.force_login(self.user1)
        update_url = reverse("label_update", kwargs={"pk": self.label1.pk})
        list_url = reverse("label_list")
        self.client.post(
            update_url,
            {"name": "Low"},
        )
        self.label1.refresh_from_db()
        self.assertEqual(self.label1.name, "Low")
        response = self.client.get(list_url)
        self.assertContains(response, "Low")
        self.assertNotContains(response, "Urgent")

    def test_delete_label(self):
        self.client.force_login(self.user1)
        delete_url = reverse("label_delete", kwargs={"pk": self.label1.pk})
        list_url = reverse("label_list")
        self.client.post(delete_url)
        response = self.client.get(list_url)
        self.assertNotContains(response, "Urgent")
