from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar_solucion, name='buscar_solucion'),
    path('contacto/', views.contacto_cliente, name='contacto_cliente'),
    
]

















