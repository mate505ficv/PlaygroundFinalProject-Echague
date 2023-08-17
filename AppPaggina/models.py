from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    curso = models.CharField(max_length=15)



class Profesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=15)



class Curso(models.Model):
    nombre = models.CharField(max_length=15)
    camada = models.CharField(max_length=15)