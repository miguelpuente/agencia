from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from apps.users.models import Perfil


class Modelo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
    
class MarcaModelo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        ordering = ('marca',)

    def __str__(self):
        return f'{self.marca} - {self.modelo}'

class Auto(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=255, unique=True)
    url = models.SlugField(max_length=255, unique=True)
    resumen = RichTextField()
    contenido = RichTextField()
    vistas = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)

    marca_modelo = models.ForeignKey(MarcaModelo, on_delete=models.PROTECT)
    visible = models.BooleanField(default=True)
    anio = models.PositiveIntegerField()
    km = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    transmision = models.CharField(max_length=20, default='Manual')
    estado = models.CharField(max_length=20, default='Disponible')
    imagen = models.ImageField(upload_to='auto/imagenes/')

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Auto, self).save(*args, **kwargs)     

    def __str__(self):
        return f'{self.marca_modelo} - {self.user.username}'


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    auto = models.ForeignKey(Auto, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=5000)
    visible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
