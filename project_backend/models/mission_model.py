from django.db import models

class Missions(models.Model):
    name = models.CharField(max_length=100)
    launch_date = models.DateField()
    agencies = models.CharField(max_length=1000)
    goals = models.CharField(max_length=6000)
    satellites = models.CharField(max_length=1000)
    sensors = models.CharField(max_length=1000)
    products = models.CharField(max_length=1000)