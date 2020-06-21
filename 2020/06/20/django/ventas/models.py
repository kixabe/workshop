from django.db import models


class Cliente(models.Model):
    dni = models.CharField('DNI', max_length=8)
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.apellidos.upper()}, {self.nombres}'


class Producto(models.Model):
    descripcion = models.CharField('descripción', max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.descripcion}'


class Venta(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    productos = models.ManyToManyField(Producto, through='DetalleVenta')

    def __str__(self):
        return f'Venta {self.id}, total {self.total}'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=7, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.producto.precio
        super().save(*args, **kwargs)
