from django.db import models

# Create your models here.

class Department(models.Model):
  name = models.CharField(max_length=20, unique=True)
  abbreviation = models.CharField(max_length=3, unique=True)
