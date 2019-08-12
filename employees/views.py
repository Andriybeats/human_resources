from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from employees.serializers import *
from employees.models import Employee

class EmployeeCreateView(generics.CreateAPIView):
  serializer_class = EmployeeDetailSerializer

class EmployeeListView(generics.ListAPIView):
  serializer_class = EmployeeDetailSerializer
  queryset = Employee.objects.all()

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = EmployeeListSerializer
  queryset = Employee.objects.all()