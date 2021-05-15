from django.contrib import admin

from .models import Area, Sexo, Carrera, Laboratorio, Modalidad, Turno, Asignatura,\
Marca, Modelo, Color, Estado

admin.site.register(Area)
admin.site.register(Sexo)
admin.site.register(Laboratorio)
admin.site.register(Modalidad)
admin.site.register(Turno)
admin.site.register(Asignatura)

# Clases ModelAdmin inventario
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display=("modelo","marca")
    list_filter=("modelo","marca")
    search_fields=("modelo",)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_filter=("marca",)
    search_fields=("marca",)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_filter=("color",)
    search_fields=("color",)

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_filter=("estado",)
    search_fields=("estado",)


# Clases ModelAdmin prestamo-reservas
class CarreraAdmin(admin.ModelAdmin):
    list_display=["carrera","area"]
    list_editable=["area"]
    search_fields=["carrera"]

admin.site.register(Carrera,CarreraAdmin)
