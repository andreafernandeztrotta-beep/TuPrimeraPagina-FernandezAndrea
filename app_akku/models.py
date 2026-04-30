from django.db import models

class Prospecto(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    email = models.EmailField()
    interes = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.empresa})"

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_servicio

class Estrategia(models.Model):
    titulo = models.CharField(max_length=100)
    detalle = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    
    
    