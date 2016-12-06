from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=30)
    result = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    link = models.CharField(max_length=30)    
    
    
    
