from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from positions.serializers import *
from positions.models import Position

class PositionCreateView(generics.CreateAPIView):
  serializer_class = PositionDetailSerializer

class PositionListView(generics.ListAPIView):
  serializer_class = PositionListSerializer
  queryset = Position.objects.all()

class PositionDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PositionListSerializer
  queryset = Position.objects.all()
