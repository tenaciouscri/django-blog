from django.test import TestCase
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone


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
            "/admin/blog/blog/add/", {"author": "1", "title": "Some title", "body": "<p>Some body</p>", "created_date_0": "2021-12-07", "created_date_1": "09:57:39", "initial-created_date_0": "2021-12-07", "initial-created_date_1": "09:57:39", "published_date_0": "2021-12-07", "published_date_1": "09:59:01", "_save": "Save"}
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/")
        self.assertTrue("Some title" in str(response.content))
    
    def test_add_comment(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            "/admin/blog/comment/add/", {"blog": "8", "author": "Some author", "body": "Some comment", "created_date_0": "2021-12-07", "created_date_1": "12:07:46", "initial-created_date_0": "2021-12-07", "initial-created_date_1": "12:07:46", "approved_comment": "on", "_save": "Save"}
        )
        print(response.content)
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/blog/8/")
        self.assertTrue("Some title" in str(response.content))
