# Generated by Django 5.0.1 on 2024-01-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_alter_hero_id_bladeicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='resume_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
