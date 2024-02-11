from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)

    projects = models.ManyToManyField("LargeProject", related_name="projects", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class LargeProject(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    date_created = models.CharField(max_length=200,null=True)
    due_date = models.CharField(max_length=200,null=True)

    sub_projects = models.ManyToManyField("SubProject", related_name="sub_projects", blank=True)


class SubProject(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    
    
