from rest_framework import serializers
from vacations.models import Vacation

class VacationDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vacation
    fields = '__all__'

class VacationListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vacation
    fields = '__all__'
