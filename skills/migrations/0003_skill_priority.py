# Generated by Django 3.2.1 on 2024-01-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_skillscategory_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]