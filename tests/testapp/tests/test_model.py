from django.core.exceptions import ValidationError
from django.test import TestCase

from django_generic_contact.models import Contact, GENERIC_CONTACT_DATA_SCHEMA
from django_generic_contact.validators import JSONSchemaValidator


class TestModel(TestCase):
    def test_successful_contact_creation(self):
        Contact.objects.create(
            name="Mr. Tester",
            message="Please contact me via email or phone.",
            data={
                "email": "mr@tester.com",
                "phone": "123456",
            }
        )

        self.assertEqual(Contact.objects.count(), 1)


class TestJsonSchema(TestCase):
    def test_successful_jsonschema_validation(self):
        validator = JSONSchemaValidator(limit_value=GENERIC_CONTACT_DATA_SCHEMA)
        validator({
            "email": "mr@tester.com",
            "not_validated_phone": "+431234567",
        })

    def test_failed_jsonschema_validation_invalid_email(self):
        validator = JSONSchemaValidator(limit_value=GENERIC_CONTACT_DATA_SCHEMA)
        with self.assertRaises(
                ValidationError,
                msg="'invalid_email' is not a 'email'\n\n"
                    "Failed validating 'format' in schema['properties']['email']:\n"
                    "    {'format': 'email', 'type': 'string'}\n\n"
                    "On instance['email']:\n"
                    "    'invalid_email'"
        ):
            validator({
                "email": "invalid_email",
                "not_validated_phone": "+431234567",
            })

    def test_failed_jsonschema_validation_additional_fields(self):
        test_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "email": {"type": "string", "format": "email"},
                "phone": {"type": "integer"},
            },
        }
        validator = JSONSchemaValidator(limit_value=test_schema)
        with self.assertRaises(
                ValidationError,
                msg="'+431234567' is not of type 'integer'\n\n"
                    "Failed validating 'type' in schema['properties']['phone']:\n"
                    "    {'type': 'integer'}\n\n"
                    "On instance['phone']:\n"
                    "    '+431234567'"
        ):
            validator({
                "email": "mr@tester.com",
                "phone": "+431234567",
            })
