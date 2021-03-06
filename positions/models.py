from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=30, unique=True)
    sallary = models.FloatField()
    vacation_days = models.IntegerField()

    def __str__(self):
      return self.name
