from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_akku.urls')), # Esto conecta tus páginas de Akkü
]

