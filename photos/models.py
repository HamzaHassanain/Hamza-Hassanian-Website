from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.uploader import destroy
from django.db.models.signals import pre_delete

# Create your models here.
class Photo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    cloudinary_image = CloudinaryField('image' , blank=True) 

    @property
    def image_url(self):
        return self.cloudinary_image.url


    def __str__(self):
        return self.name
    
def delete_cloudinary_image(sender, instance, **kwargs):
    image_public_id = instance.cloudinary_image.public_id
    destroy(image_public_id)
    
pre_delete.connect(delete_cloudinary_image, sender=Photo)