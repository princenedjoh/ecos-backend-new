from django.db import models
from . import users_model, article_model

class Article_like(models.Model):
    user = models.ForeignKey(
        users_model.Users,
        on_delete=models.SET_NULL,
        null=True
    )
    article = models.ForeignKey(
        article_model.Article,
        on_delete=models.SET_NULL,
        null=True
    )