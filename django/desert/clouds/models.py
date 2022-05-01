from distutils.command.upload import upload
from django.db import models
from matplotlib import image

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    age = models.CharField(max_length=50,default="")
    date_of_birth = models.CharField(max_length=50,default="")    
    disc = models.TextField()
   
    def __str__(self):
        return self.name

class image(models.Model):
    name = models.CharField(max_length=50,default="")
    photo= models.ImageField(upload_to="images")
    date=  models.DateTimeField(auto_now_add="True")
    def __str__(self):
        return self.name

class imageuploader(models.Model):
    name = models.CharField(max_length=50,default="")
    photo= models.ImageField(upload_to="images")
    date=  models.DateTimeField(auto_now_add="True")
    desc=  models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name