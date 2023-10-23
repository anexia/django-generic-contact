from django.conf import settings
from django.test import SimpleTestCase


class TestSetup(SimpleTestCase):
    def test_installed_apps(self):
        self.assertIn("django_generic_contact", settings.INSTALLED_APPS)
