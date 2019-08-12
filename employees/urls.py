from django.contrib import  admin
from django.urls import path, include
from employees.views import *

app_name = 'employee'

urlpatterns = [
  path('create', EmployeeCreateView.as_view()),
  path('all', EmployeeListView.as_view()),
  path('<int:pk>', EmployeeDetailView.as_view())
]