from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from vacations.serializers import *
from vacations.models import Vacation

class VacationCreateView(generics.CreateAPIView):
  serializer_class = VacationDetailSerializer

class VacationListView(generics.ListAPIView):
  serializer_class = VacationListSerializer
  queryset = Vacation.objects.all()

class VacationDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = VacationListSerializer
  queryset = Vacation.objects.all()