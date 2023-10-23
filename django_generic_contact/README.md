# Schema configuration

The `data` field on the `Contact` model can be optionally extended by providing a Schema according to
[jsonschema](https://json-schema.org/)

```
GENERIC_CONTACT_DATA_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "email": {
            "format": "email"
        },
    },
    "unevaluatedProperties": {
        "type": ["integer", "string"]
    }
}
```

The app makes use of the [python implementation](https://python-jsonschema.readthedocs.io/en/stable/) of jsonschema
and supports format checking according to the library implementation.
