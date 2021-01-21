from django.db import models
from django.utils.dateformat import DateFormat

# Create your models here.

class Session_form (models.Model) : 
    session_date = models.DateField(null=True, blank=True, auto_now_add=False)
    title = models.CharField(null=True, max_length=20)

    def __str__ (self) :
        return self.title