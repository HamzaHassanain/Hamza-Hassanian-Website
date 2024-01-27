from django.db import models

# Create your models here.
class SkillsCategory(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    # description=models.TextField(blank=True)
    category_id=models.ForeignKey('SkillsCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name