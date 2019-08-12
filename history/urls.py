from django.contrib import admin
from django.urls import path, include
from history.views import *

app_name = 'history'

urlpatterns = [
  path('create', HistoryCreateView.as_view()),
  path('all', HistoryListView.as_view()),
  path('<int:pk>', HistoryDetailView.as_view())
]