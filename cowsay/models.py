from django.db import models

# Create your models here.

class Cow(models.Model):
    text = models.CharField(max_length=100)
    output = models.TextField()
    