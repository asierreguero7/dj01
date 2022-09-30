from django.db import models

# Create your models here.

class Platera(models.Model):
    izena = models.TextField()
    prezioa = models.FloatField()
    