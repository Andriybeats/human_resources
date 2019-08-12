from django.db import models
from employees.models import Employee
# Create your models here.

class Vacation(models.Model):
  date_start = models.DateField()
  date_end = models.DateField()
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)