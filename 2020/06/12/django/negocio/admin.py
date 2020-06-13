from django.contrib import admin

from .models import Pregunta, Alternativa, Persona


class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 1


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['texto', 'fecha']
    inlines = [AlternativaInline]
    search_fields = ['texto']
    list_filter = ['fecha']


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass
