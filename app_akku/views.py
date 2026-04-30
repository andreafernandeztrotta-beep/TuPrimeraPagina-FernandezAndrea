from django.shortcuts import render, redirect
from .models import Servicio, Estrategia, Cliente

def index(request):
    return render(request, 'app_akku/index.html')

def buscar_solucion(request):
    query = request.GET.get('q', '')
    servicios = Servicio.objects.filter(nombre__icontains=query) if query else []
    estrategias = Estrategia.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'app_akku/buscar.html', {'servicios': servicios, 'estrategias': estrategias, 'query': query})

def contacto_cliente(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        Cliente.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        return redirect('index')
    return render(request, 'app_akku/prospecto_form.html')











    
    
