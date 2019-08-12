from django.contrib import admin
from django.urls import path, include
from positions.views import *

app_name = 'position'

urlpatterns = [
  path('create', PositionCreateView.as_view()),
  path('all', PositionListView.as_view()),
  path('<int:pk>', PositionDetailView.as_view())
]