from django.contrib import  admin
from django.urls import path, include
from departments.views import *

app_name = 'department'

urlpatterns = [
  path('create', DepartmentCreateView.as_view()),
  path('all', DepartmentListView.as_view()),
  path('<int:pk>', DepartmentDetailView.as_view())
]