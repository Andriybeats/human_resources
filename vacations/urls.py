from django.contrib import admin
from django.urls import path, include
from vacations.views import *

app_name = 'vacation'

urlpatterns = [
  path('create', VacationCreateView.as_view()),
  path('all', VacationListView.as_view()),
  path('<int:pk>', VacationDetailView.as_view())
]