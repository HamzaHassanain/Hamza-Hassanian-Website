# Generated by Django 3.2.1 on 2024-01-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalproject',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]