from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Columnas mostradas
    search_fields = ('nombre',)      # Barra de búsqueda por nombre
    list_filter = ('nombre',)        # Filtros por nombre

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')  # Columnas personalizadas
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio', 'f_fabricacion')  # Filtros por laboratorio y fecha
    search_fields = ('nombre',)
