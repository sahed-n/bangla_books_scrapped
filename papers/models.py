from django.db import models

class Paper(models.Model):
  name = models.CharField(max_length=255)
  author = models.CharField(max_length=800)
  abstract = models.CharField(max_length=2000)
  link = models.CharField(max_length=255, default='alink')
  #citations =
