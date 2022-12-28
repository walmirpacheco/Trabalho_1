from django.urls import path

from .views import index, funcionario, cliente

urlpatterns = [
    path('', index, name='index'),
    path('funcionario/<int:pk>', funcionario, name='funcionario'),
    path('cliente/<int:pk>', cliente, name='cliente')     
]