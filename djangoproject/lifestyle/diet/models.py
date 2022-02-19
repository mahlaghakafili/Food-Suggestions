from django.db import models


class User(models.Model):
    objects = None
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    bmi = models.IntegerField()
    name = models.TextField(max_length=100)
    fname = models.TextField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    veg_type = models.TextField()
