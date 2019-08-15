from django.db import models
from departments.models import Department
from positions.models import Position
from django.core.validators import EmailValidator


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    date_birthaday = models.DateField()
    city_birthday = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    start_work = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee/images/', )

    def __str__(self):
        return self.name
