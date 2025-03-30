from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    profile_picture = models.CharField(max_length=1000, null=True)
    gender = models.CharField(max_length=100, null=True)