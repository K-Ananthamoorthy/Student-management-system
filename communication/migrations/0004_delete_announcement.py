# Generated by Django 5.1.1 on 2024-10-23 01:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("communication", "0003_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Announcement",
        ),
    ]
