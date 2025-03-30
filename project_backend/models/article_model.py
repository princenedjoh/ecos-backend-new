from django.db import models
from . import users_model, article_category_model

class Article(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=1000)
    content = models.CharField(max_length=6000)
    author = models.ForeignKey(
        users_model.Users, 
        on_delete=models.SET_NULL, 
        null=True
    )
    category = models.ForeignKey(
        article_category_model.Article_category,
        on_delete=models.SET_NULL,
        null=True
    )
    cover_image = models.CharField(max_length=200)
    tags = models.TextField()