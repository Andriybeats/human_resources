from rest_framework import serializers
from history.models import History

class  HistoryDetailSerilizer(serializers.ModelSerializer):
  class Meta:
    model = History
    fields = "__all__"

class HistoryListSerializer(serializers.ModelSerializer):
  class Meta:
    model = History
    fields = '__all__'
