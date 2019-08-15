from rest_framework import serializers
from departments.models import Department

class CreateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        department = Department.objects.all()
        return department

class DepartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
      model = Department
      fields = ('id', 'name', 'abbreviation')

class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
