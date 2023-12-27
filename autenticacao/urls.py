from django.urls import path
from . import views


urlpatterns = [
    path('lodin/',views.login,name='login'),
    path('register/',views.cadastro,name='register'),
    path('logout/',views.sair,name='sair'),
]
