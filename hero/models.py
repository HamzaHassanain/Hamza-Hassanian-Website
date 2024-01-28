from django.db import models
from django.core.exceptions import ValidationError
import cloudinary
# Create your models here.

class BladeIcon(models.Model):
    link=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    blade_icon_code=models.CharField(max_length=100)
    hero_id=models.ForeignKey('Hero', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hero(models.Model):
    id=models.AutoField(primary_key=True)
    slug=models.CharField(max_length=100)
    small_title=models.CharField(max_length=100)
    big_title=models.CharField(max_length=100)
    about_me=models.TextField(blank=True)
    resume_url=models.CharField(max_length=200, blank=True)
    image = cloudinary.models.CloudinaryField('image')

    def save(self, *args, **kwargs):
        if not self.id and Hero.objects.exists():
            raise ValidationError('There is can be only one Hero instance')
        return super(Hero, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.slug