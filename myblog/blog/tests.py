from django.test import TestCase
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser", password="password"
        )

    def tearDown(self):
        self.user.delete()

    def test_add_blog_post(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            "/admin/blog/blog/add/", {"title": "TEST TITLE", "body": "TEST BODY"}
        )
        print(response.content)
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/")
        self.assertTrue("TEST TITLE" in str(response.content))