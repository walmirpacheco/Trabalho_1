from django.urls import path

from .views import index, funcionarios

urlpatterns = [
    path('', index),
    path('funcionarios', funcionarios),       
]