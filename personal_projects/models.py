from django.db import models
from django import forms
from cloudinary.models import CloudinaryField

# Create your models here.

class BigTextField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = forms.Textarea(attrs={'rows':40, 'cols':100})
        return super(BigTextField, self).formfield(**kwargs)

class PersonalProject(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100 , blank=True)
    title=models.CharField(max_length=100,blank=True)
    slug=models.CharField(max_length=100)
    small_description=models.TextField(blank=True)
    description=BigTextField(blank=True)

    priority=models.IntegerField(default=0)
    thumbnail=CloudinaryField('image',blank=True)
    def __str__(self):
        return self.title