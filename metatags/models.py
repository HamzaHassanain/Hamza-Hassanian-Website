from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

class MetaTags(models.Model):
    title = models.CharField(max_length=100 , default="My Portfolio")
    description = models.CharField(max_length=200 , default="My Portfolio")
    keywords = models.CharField(max_length=200 , default="portfolio, resume, cv")
    author = models.CharField(max_length=100 , default="Hamza Hassanain")
    image = CloudinaryField('image' , blank=True)
    url = models.URLField(max_length=200 , default="https://hamzahassanain.onrender.com")
    site_name = models.CharField(max_length=100 , default="Hamza Hassanain Resume")
    type = models.CharField(max_length=100 , default="website")
    twitter_creator = models.CharField(max_length=100 , default="@hamzahasa067")

    # make sure only one instance of this model is created
    def save(self, *args, **kwargs):
        if not self.pk and MetaTags.objects.exists():
            raise ValidationError('There can only be one MetaTags instance')
        return super(MetaTags, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title + " Meta Tags"