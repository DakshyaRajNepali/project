# Generated by Django 5.1.7 on 2025-03-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_flash_sale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(default="Unnamed Product", max_length=100),
        ),
    ]
