from django.db import models
from . import users_model
from project_backend.types import types

class Settings(models.Model):
    user = models.ForeignKey(
        users_model.Users, 
        on_delete=models.CASCADE,
    )
    name =  models.CharField(
        max_length=100,
        choices=types.settings
    )
    value = models.CharField(max_length=1000)