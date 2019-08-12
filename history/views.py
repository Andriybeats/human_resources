from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from history.serializers import *
from history.models import History

class HistoryCreateView(generics.CreateAPIView):
  serializer_class = HistoryDetailSerilizer

class HistoryListView(generics.ListAPIView):
  serializer_class = HistoryListSerializer
  queryset = History.objects.all()

class HistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = HistoryListSerializer
  queryset = History.objects.all()
