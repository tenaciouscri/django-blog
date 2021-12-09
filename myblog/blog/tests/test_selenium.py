import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumTest(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        if os.getenv("CI"):
            options.binary_location = "/usr/bin/google-chrome-stable"
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            self.driver = webdriver.Chrome(options=options)
        else:
            from chromedriver_binary import chromedriver_filename

            self.driver = webdriver.Chrome(chromedriver_filename, options=options)
        self.user = User.objects.create_superuser(
            username="testuser", password="password"
        )

    def tearDown(self):
        self.user.delete()

    def test_add_blog_post(self):
        self.driver.get(f"{self.live_server_url}/admin/")
        username_field = self.driver.find_element_by_id("id_username")
        username_field.send_keys("testuser")
        password_field = self.driver.find_element_by_id("id_password")
        password_field.send_keys("password")
        login_button = self.driver.find_element_by_css_selector(
            "#login-form > div.submit-row > input[type=submit]"
        )
        login_button.click()
        add_blog_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    (
                        "#content-main > div.app-blog.module > "
                        "table > tbody > tr > td:nth-child(2) > a"
                    ),
                )
            )
        )
        add_blog_button.click()
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "id_title"))
        )
        title_fields = self.driver.find_elements_by_css_selector("#id_title")
        self.assertEqual(len(title_fields), 1)
