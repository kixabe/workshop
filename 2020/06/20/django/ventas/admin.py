from django.contrib import admin

from .models import Cliente, Producto, Venta


admin.site.site_url = None # null
admin.site.site_header = 'Hola Mundo'


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'dni', 'nombres', 'apellidos']
    list_display_links = ['dni', 'nombres', 'apellidos']
    search_fields = ['dni', 'nombres', 'apellidos']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'precio', 'activo']
    search_fields = ['descripcion']


class DetalleVentaInline(admin.TabularInline):
    model = Venta.productos.through
    autocomplete_fields = ['producto']
    extra = 3


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cliente']
    inlines = [DetalleVentaInline]
    list_display_links = ['fecha']
    list_filter = ['fecha', 'cliente']
    list_display = ['id', 'fecha', 'cliente', 'total']

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        total = 0
        venta = form.instance
        for detalle in venta.detalleventa_set.all():
            total += detalle.total
        venta.total = total
        venta.save()
