from rest_framework import serializers
from positions.models import Position

class PositionDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'

class PositionListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'