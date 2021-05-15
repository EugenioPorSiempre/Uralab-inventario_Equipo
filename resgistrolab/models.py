from django.db import models
from catalogos.models import Sexo, Area, Carrera, Asignatura, Modalidad, Turno, Laboratorio


class Usuario(models.Model):
    usuario = models.CharField(max_length=70)

    def __str__(self):
        return self.usuario


class Curso(models.Model):
    nom_practica = models.CharField(max_length=70)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    ano = models.CharField(max_length=70)
    semestre = models.CharField(max_length=70)

    def __str__(self):
        return self.nom_practica


class PrestamoLaboratorio(models.Model):
    descripcion = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    fecha = models.DateField(max_length=20)
    cantidad_horas = models.CharField(max_length=70)

    def __str__(self):
        return self.descripcion


class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(
        PrestamoLaboratorio, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=70)

    def __str__(self):
        return self.cantidad
