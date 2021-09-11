from django.contrib import admin
from django.urls import path,include
from .views import HomeView

app_name = 'tracker'

urlpatterns = [
    path('',HomeView,name='home'),
]
