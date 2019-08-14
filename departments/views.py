from rest_framework import generics

from departments.models import Department
from departments.serializers import *


class DepartmentCreateView(generics.CreateAPIView):
  serializer_class = DepartmentDetailSerializer

class DepartmentListView(generics.ListAPIView):
  serializer_class = DepartmentListSerializer
  queryset = Department.objects.all()

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = DepartmentListSerializer
  queryset = Department.objects.all()


