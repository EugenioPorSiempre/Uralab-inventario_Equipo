from django.contrib import admin

# Register your models here.
from .models import Reservaciones
class ReservasAdmin(admin.ModelAdmin):
    list_filter=["fecha"]

admin.site.register(Reservaciones,ReservasAdmin)
