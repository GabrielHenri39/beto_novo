from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_cliente/', views.cadastra_cliente, name='cadastro_cliente'),

]


