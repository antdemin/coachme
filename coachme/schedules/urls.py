from django.contrib import admin
from django.urls import include, path

from .views import Schedule

app_name = 'schedule'

urlpatterns = [
    path('delete/<int:pk>/', Schedule.as_view(), { 'delete': True }, name='delete'),
    path('<slug:username>/', Schedule.as_view(), name='coach'),
    path('', Schedule.as_view(), name='user'),
]
