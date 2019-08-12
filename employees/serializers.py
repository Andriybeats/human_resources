from rest_framework import serializers
from employees.models import Employee

class EmployeeDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'

class EmployeeListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'
