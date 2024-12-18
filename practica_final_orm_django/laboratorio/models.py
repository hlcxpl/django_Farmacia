from django.db import models

# Modelo Laboratorio
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo
    pais = models.CharField(max_length=100, blank=True, null=True)    # Nuevo campo

    def __str__(self):
        return self.nombre

# Modelo Director General
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio.nombre}"

# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos')
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
