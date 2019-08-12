from django.db import models
from employees.models import Employee
from positions.models import Position

# Create your models here.

class History(models.Model):
  data_start = models.DateField()
  data_end = models.DateField()
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  position = models.ForeignKey(Position, on_delete=models.CASCADE)