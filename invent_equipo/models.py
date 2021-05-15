from django.db import models
from catalogos.models import Modelo, Color, Estado, Laboratorio
# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=70)
    serie = models.CharField(max_length=70)
    cod_inventario = models.IntegerField()
    descripcion = models.CharField(max_length=70)

    modelo= models.ForeignKey(Modelo, on_delete=models.CASCADE)
    color= models.ForeignKey(Color, on_delete=models.CASCADE)
    estado= models.ForeignKey(Estado, on_delete=models.CASCADE)
    laboratorio= models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    padre= models.OneToOneField('Equipo', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

