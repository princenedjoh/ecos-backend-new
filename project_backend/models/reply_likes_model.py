from django.db import models
from . import users_model, reply_model

class Reply_like(models.Model):
    user = models.ForeignKey(
        users_model.Users,
        on_delete=models.SET_NULL,
        null=True
    )
    reply = models.ForeignKey(
        reply_model.Reply,
        on_delete=models.SET_NULL,
        null=True
    )