from django.contrib import  admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from departments.views import *

app_name = 'department'

urlpatterns = [
  path('create/', CreateDepartmentAPIView.as_view()),
  path('all/', DepartmentListAPIView.as_view()),
  path('<int:pk>/', DepartmentDetailAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
