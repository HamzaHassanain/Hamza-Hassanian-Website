from django.db import models

# Create your models here.
class ExperienceCategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    priority=models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class Experience(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100,blank=True)
    subtitle=models.CharField(max_length=100 , blank=True)
    description=models.TextField(blank=True)
    start_date=models.CharField(max_length=100)
    end_date=   models.CharField(max_length=100)
    category_id=models.ForeignKey('ExperienceCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name