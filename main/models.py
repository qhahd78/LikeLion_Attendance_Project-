from django.db import models

# Create your models here.

class Student (models.Model) : 
    name = models.CharField(max_length=5)
    phone_num = models.CharField(max_length=11)
    major = models.CharField(max_length=15)
    profile = models.ImageField(upload_to="image", default=None)

    def __str__ (self): 
        return self.name

    