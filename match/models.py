from django.db import models
from django.contrib.auth.models import User

class ImagenFondo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes_fondo/')

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField(max_length=200, blank=True, null=True)
    imagen_fondo = models.ForeignKey(ImagenFondo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    label = models.CharField(max_length=100, unique=True, blank=True, null=True)
    texto = models.TextField()

    def __str__(self):
        return self.label if self.label else self.texto


class AnoAcademico(models.Model):
    nombre = models.CharField(max_length=50)  # Por ejemplo, "5to básico", "4to medio"
    pregunta_inicial = models.ForeignKey(Pregunta, null=True, blank=True, on_delete=models.SET_NULL)
    #curso destino opcional
    curso_destino = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

class Opcion(models.Model):
    pregunta_origen = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    siguiente_pregunta = models.ForeignKey(Pregunta, null=True, blank=True, on_delete=models.SET_NULL)
    curso_destino = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.texto

class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
