# Generated by Django 5.1.5 on 2025-03-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(max_length=20),
        ),
    ]
