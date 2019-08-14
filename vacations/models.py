from django.db import models
from employees.models import Employee
from vacations.validators import *


class Vacation(models.Model):
    date_start = models.DateField(validators=[validate_start_date])
    date_end = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
