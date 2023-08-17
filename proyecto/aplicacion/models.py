from django.db import models
# Create your models here.
class Celular(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()

class TV (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    pulgadas = models.IntegerField()
    precio = models.IntegerField()

class PC (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    disco = models.CharField(max_length=50)
    pulgadas = models.IntegerField()
    precio = models.IntegerField()
