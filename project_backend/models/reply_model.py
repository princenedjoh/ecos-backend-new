from django.db import models
from . import users_model, comment_model

class Reply(models.Model):
    user = models.ForeignKey(
        users_model.Users, 
        on_delete=models.SET_NULL, 
        null=True
    )
    comment = models.ForeignKey(
        comment_model.Comment, 
        on_delete=models.SET_NULL, 
        null=True
    )
    reply = models.CharField(max_length=200)