# Generated by Django 3.2.1 on 2024-01-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_hero_resume_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bladeicon',
            old_name='blad_icon_code',
            new_name='blade_icon_code',
        ),
    ]
