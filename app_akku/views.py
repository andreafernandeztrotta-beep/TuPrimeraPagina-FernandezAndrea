from django.shortcuts import render
from .models import Servicio, Estrategia

def index(request):
    """Página principal de Akkü Studio Lab"""
    return render(request, 'app_akku/index.html')

def buscar_solucion(request):
    """Buscador exclusivo para Data y Growth"""
    query = request.GET.get('q', '')
    if query:
        # Filtramos solo por lo que el usuario busca, sin sugerencias de UX
        servicios = Servicio.objects.filter(nombre__icontains=query)
        estrategias = Estrategia.objects.filter(nombre__icontains=query)
    else:
        servicios = Servicio.objects.none()
        estrategias = Estrategia.objects.none()
    
    return render(request, 'app_akku/buscar.html', {
        'servicios': servicios,
        'estrategias': estrategias,
        'query': query
    })

def contacto_cliente(request):
    """Formulario de consultas - Usando el archivo real prospecto_form.html"""
    return render(request, 'app_akku/prospecto_form.html')


    

    

    





    



    
    
