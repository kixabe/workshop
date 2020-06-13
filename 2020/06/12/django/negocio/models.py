from django.db import models


class Pregunta(models.Model):
    texto = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.texto


class Alternativa(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.PROTECT)
    texto = models.CharField(max_length=50)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto


class Persona(models.Model):
    dni = models.CharField(max_length=8)
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    foto = models.ImageField()

    def __str__(self):
        return f"{self.apellidos.upper()}, {self.nombres}"
