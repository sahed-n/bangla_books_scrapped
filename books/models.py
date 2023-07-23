from django.db import models

class Book(models.Model):
  name = models.CharField(max_length=255)
  writer = models.CharField(max_length=255)
  rating = models.FloatField()
  price = models.FloatField()
  link = models.CharField(max_length=255, default='alink')