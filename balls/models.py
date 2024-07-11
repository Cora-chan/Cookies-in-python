from django.db import models

# Create your models here.

class Report(models.Model):
    user = models.CharField(unique=True, max_length=36)
    color = models.CharField(max_length=128)
    count = models.IntegerField()