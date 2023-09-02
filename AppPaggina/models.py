from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    curso = models.CharField(max_length=15)

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='tareas/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=15)



class Curso(models.Model):
    nombre = models.CharField(max_length=15)
    camada = models.CharField(max_length=15)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user}  -  {self.imagen}"
    
