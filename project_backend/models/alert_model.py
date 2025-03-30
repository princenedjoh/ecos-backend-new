from django.db import models
from . import users_model
from project_backend.types import types

class Alert(models.Model):
    user = models.ForeignKey(
        users_model.Users, 
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField()
    read = models.BooleanField(default=False)
    severity = models.CharField(
        max_length=20,
        choices=types.severity
    )
    category = models.CharField(
        max_length=20,
        choices=types.alert_category
    )
    image = models.CharField(max_length=500, null=True)
    data = models.CharField(max_length=5000, null=True)