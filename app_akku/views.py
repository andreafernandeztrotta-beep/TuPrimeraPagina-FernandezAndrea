from django.shortcuts import render
from .models import Prospecto, Servicio, Curso

def inicio(request):
    return render(request, 'app_akku/inicio.html')

def nuevo_prospecto(request):
    return render(request, 'app_akku/prospecto_form.html')

def nuevo_servicio(request):
    return render(request, 'app_akku/servicio_form.html')

def nuevo_curso(request):
    return render(request, 'app_akku/curso_form.html')

def buscar_prospecto(request):
    return render(request, 'app_akku/buscar.html')
















    
    
