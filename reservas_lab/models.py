from django.db import models

# Create your models here.
from catalogos.models import Turno, Laboratorio, Modalidad, Asignatura,Carrera, Area
from resgistrolab.models import Usuario

class Reservaciones(models.Model):
    nombre_practica=models.CharField(max_length=70)
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    turno=models.ForeignKey(Turno, on_delete=models.CASCADE)
    area=models.ForeignKey(Area, on_delete=models.CASCADE)
    modalidad=models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    asignatura=models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(max_length=20)
    hora_inicio=models.TimeField(max_length=30)
    hora_fin=models.TimeField(max_length=30)
    
    def __str__(self):
        return self.nombre_practica

    