from django.db import models

class Platerak(models.Model):
  izena = models.CharField(max_length=255)
  prezioa = models.FloatField()
    