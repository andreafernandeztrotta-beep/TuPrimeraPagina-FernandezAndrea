from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Estrategia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    
    
    
    
    
    