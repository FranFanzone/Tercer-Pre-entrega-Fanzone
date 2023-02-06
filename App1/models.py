from django.db import models

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    materia = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(default='0000-00-00')
    email = models.EmailField()

class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    materia = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(default='0000-00-00')
    email = models.EmailField()

class Carrera(models.Model):

    nombre = models.CharField(max_length=40)
    materias = models.CharField(max_length=40)

class Entregable(models.Model):

    materia = models.CharField(max_length=40)
    entregado = models.BooleanField()
