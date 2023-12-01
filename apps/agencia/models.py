from django.db import models

class Modelo(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class MarcaModelo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.marca} - {self.modelo}'

class Auto(models.Model):
    marca_modelo = models.ForeignKey(MarcaModelo, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    anio = models.PositiveIntegerField()
    km = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    transmision = models.CharField(max_length=20, default='Manual')
    estado = models.CharField(max_length=20, default='Disponible')
    imagen = models.ImageField(upload_to='auto_images/')

    def __str__(self):
        return f'{self.marca_modelo} - {self.anio} - {self.color}'


