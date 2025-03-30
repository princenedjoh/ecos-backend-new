from django.db import models

class Article_category(models.Model):
    name = models.CharField(max_length=20)