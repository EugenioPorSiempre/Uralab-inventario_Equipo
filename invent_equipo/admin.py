from django.contrib import admin

from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display=("nombre","serie","cod_inventario","descripcion","modelo","color","estado","laboratorio")
    list_filter=("nombre","cod_inventario")
    search_fields=['nombre',]
    list_editable=("estado","laboratorio")