# Generated by Django 5.0.3 on 2024-03-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FrontEnd", "0014_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="Username",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
