from rest_framework import serializers
from departments.models import Department

class DepartmentDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ('id', 'name', 'abbreviation')

class DepartmentListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = '__all__'