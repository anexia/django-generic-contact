# Generated by Django 3.2.8 on 2021-10-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_generic_contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(blank=True, verbose_name="message"),
        ),
    ]
