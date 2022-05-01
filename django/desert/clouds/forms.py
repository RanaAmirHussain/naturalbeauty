
from clouds.models import imageuploader
from django.db import models

class imageuploader(models.Model):
    name = models.CharField(max_length=50,default="")
    photo= models.ImageField(upload_to="images")
    date=  models.DateTimeField(auto_now_add="True")
    desc=  models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name
    
    
    