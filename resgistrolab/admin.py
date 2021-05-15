from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Usuario, Curso, PrestamoLaboratorio, DetallePrestamo


class DetallesPrestamos(admin.TabularInline):
    model=DetallePrestamo
    extra=0

class PrestamoLaboratorioAdmin(admin.ModelAdmin):
    list_display=["descripcion","curso","usuario","laboratorio","fecha","cantidad_horas"]
    #list_editable=["curso","usuario","laboratorio","fecha","cantidad_horas"]
    list_filter=["laboratorio"]
    inlines=[DetallesPrestamos]

class CursoAdmin(admin.ModelAdmin):
    list_display=["nom_practica","asignatura","modalidad","carrera","ano","semestre"]
    list_editable=["asignatura","modalidad","carrera","ano","semestre"]
    list_filter=["carrera","modalidad"]

class DetallePrestamoAdmin(admin.ModelAdmin):
    list_display=["prestamo","sexo","cantidad"]
    list_editable=["sexo","cantidad"]



admin.site.register(Usuario)
admin.site.register(Curso,CursoAdmin)
admin.site.register(PrestamoLaboratorio,PrestamoLaboratorioAdmin)
admin.site.register(DetallePrestamo,DetallePrestamoAdmin)
# Register your models here.