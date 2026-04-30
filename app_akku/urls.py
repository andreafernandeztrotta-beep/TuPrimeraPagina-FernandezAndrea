from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('consulta/', views.nueva_consulta, name='nueva_consulta'),
    path('buscar/', views.buscar_prospecto, name='buscar_prospecto'),
]












