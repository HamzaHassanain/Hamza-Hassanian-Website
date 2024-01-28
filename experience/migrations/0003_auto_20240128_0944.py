# Generated by Django 3.2.1 on 2024-01-28 09:44

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_auto_20240127_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='experiencecategory',
            name='description',
            field=martor.models.MartorField(),
        ),
    ]
