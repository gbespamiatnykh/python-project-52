from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserModelTest(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user1.set_password("testpass1")
        self.user1.save()
        self.user2 = User.objects.get(pk=2)
        self.user2.set_password("testpass2")
        self.user2.save()

    def test_create_user(self):
        create_url = reverse("user_create")
        list_url = reverse("user_list")
        self.client.post(
            create_url,
            {
                "username": "B0bSing",
                "first_name": "Robert",
                "last_name": "Singer",
                "password1": "testpass4",
                "password2": "testpass4",
            },
        )
        response = self.client.get(list_url)
        self.assertContains(response, "B0bSing")

    def test_update_user(self):
        self.client.login(
            username="Sam83",
            password="testpass2",
        )
        update_url = reverse("user_update", kwargs={"pk": self.user2.pk})
        list_url = reverse("user_list")
        response = self.client.post(
            update_url,
            {
                "username": "Sam83",
                "first_name": "John",
                "last_name": "Winchester",
                "password1": "testpass3",
                "password2": "testpass3",
            },
        )
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.first_name, "John")
        response = self.client.get(list_url)
        self.assertContains(response, "John")
        self.assertNotContains(response, "Samuel")

    def test_delete_user(self):
        self.client.login(
            username="Soldier_boy",
            password="testpass1",
        )
        delete_url = reverse("user_delete", kwargs={"pk": self.user1.pk})
        list_url = reverse("user_list")
        self.client.post(delete_url)
        response = self.client.get(list_url)
        self.assertNotContains(response, "Soldier_boy")
