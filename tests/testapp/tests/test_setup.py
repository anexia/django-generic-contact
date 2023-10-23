from django.test import SimpleTestCase

from django.conf import settings


class TestSetup(SimpleTestCase):
    def test_installed_apps(self):
        self.assertIn("django_generic_contact", settings.INSTALLED_APPS)
