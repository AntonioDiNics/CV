from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('fruitstore/', views.fruitstore),
    path('project2/', views.project2),
]
