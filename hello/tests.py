from django.test import TestCase

from .models import Greeting


class HelloTests(TestCase):
    def test_default(self):
        self.assertContains(self.client.get("/"), "Hello, human")

    def test_admin_managed_greeting(self):
        Greeting.objects.create(message="Hi there")
        self.assertContains(self.client.get("/"), "Hi there")

    def test_admin_login_page(self):
        self.assertEqual(self.client.get("/admin/login/").status_code, 200)
