from django.shortcuts import render

def inicio(request):
    return render(request, 'app_akku/inicio.html')

def nueva_consulta(request):
    # Esta función ahora busca el formulario de consulta
    return render(request, 'app_akku/prospecto_form.html')

def buscar_prospecto(request):
    servicios = [
        {'nombre': 'Estrategia Growth', 'desc': 'Optimización científica de embudos.', 'precio': '$12.000'},
        {'nombre': 'Data Strategy', 'desc': 'Modelado de datos para negocio.', 'precio': '$15.000'},
        {'nombre': 'Auditoría UX/UI', 'desc': 'Análisis de comportamiento de usuario.', 'precio': '$8.000'},
    ]
    query = request.GET.get('nombre', '').lower()
    if query:
        resultados = [s for s in servicios if query in s['nombre'].lower() or query in s['desc'].lower()]
    else:
        resultados = servicios 
    return render(request, 'app_akku/buscar.html', {'resultados': resultados, 'query': query})















    
    
