from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    #estas son las subcarpetas que en las que se alojaran las imagenes
    url = models.URLField(blank=True)#esto hace que sea opcional