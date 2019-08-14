from django.db import models
from departments.validators import *
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(max_length=20, unique=True, validators=[validate_only_letters])
    abbreviation = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.name