# Generated by Django 5.1.5 on 2025-01-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("text", models.CharField(max_length=1000)),
                ("author", models.CharField(max_length=255)),
            ],
        ),
    ]
