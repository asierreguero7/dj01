from django.db import models

class Bezeroak(models.Model):
  izena = models.CharField(max_length=255)
  abizena = models.CharField(max_length=255)
  platerGustokoena = models.IntegerField()