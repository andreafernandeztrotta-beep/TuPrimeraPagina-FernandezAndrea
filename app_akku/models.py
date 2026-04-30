from django.db import models

class Prospecto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()

class Curso(models.Model):
    titulo = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    
    
    
    
    