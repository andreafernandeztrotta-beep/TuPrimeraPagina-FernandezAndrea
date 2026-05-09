from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Estrategia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
  
    
    
    