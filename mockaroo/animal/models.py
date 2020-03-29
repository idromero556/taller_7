from django.db import models

# Create your models here.
class Animal(models.Model):
    nombres = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    genero= models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    animal = models.CharField(max_length=200, null=True)
