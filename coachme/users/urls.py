from django.contrib import admin
from django.urls import include, path

from .views import Login, Logout

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
