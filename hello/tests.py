from django.test import TestCase

from .models import Greeting


class HelloTests(TestCase):
    def test_default(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "hello claude, I am gpt")

    def test_admin_managed_greeting(self):
        Greeting.objects.create(message="Hi there")
        self.assertContains(self.client.get("/"), "Hi there")

    def test_admin_login_page(self):
        self.assertEqual(self.client.get("/admin/login/").status_code, 200)

    def test_model_default(self):
        greeting = Greeting.objects.create()
        self.assertEqual(greeting.message, "hello claude, I am gpt")
        self.assertContains(self.client.get("/"), "hello claude, I am gpt")

    def test_inactive_greeting_uses_default(self):
        Greeting.objects.create(message="Hidden", active=False)
        self.assertContains(self.client.get("/"), "hello claude, I am gpt")

    def test_newer_inactive_greeting_does_not_override_active(self):
        Greeting.objects.create(message="Active greeting")
        Greeting.objects.create(message="Hidden", active=False)
        self.assertContains(self.client.get("/"), "Active greeting")

    def test_latest_active_greeting(self):
        Greeting.objects.create(message="Older greeting")
        Greeting.objects.create(message="Latest greeting")
        with self.assertNumQueries(1):
            response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Latest greeting")

    def test_greeting_is_plain_text(self):
        message = "<script>alert('hello')</script>"
        Greeting.objects.create(message=message)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain; charset=utf-8")
        self.assertEqual(response.content.decode(), message)

    def test_empty_active_greeting_does_not_use_default(self):
        Greeting.objects.create(message="")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")
