# Generated by Django 3.2.1 on 2024-01-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='experience',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]