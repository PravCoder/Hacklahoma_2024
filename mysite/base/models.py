from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)

"""

class Project(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)

class SubProject(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    
    
"""
