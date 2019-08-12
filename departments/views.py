from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from departments.serializers import *
from departments.models import Department

class DepartmentCreateView(generics.CreateAPIView):
  serializer_class = DepartmentDetailSerializer

class DepartmentListView(generics.ListAPIView):
  serializer_class = DepartmentListSerializer
  queryset = Department.objects.all()

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = DepartmentListSerializer
  queryset = Department.objects.all()