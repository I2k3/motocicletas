
from django.db import models

# Create your models here 

class Motocicleta(models.Model):

    description = models.TextField(blank=True)
    marca = models.TextField(default='',blank=False)
    modelo = models.TextField(default='',blank=False)
    motor = models.TextField(default='',blank=False)
    consumo_g= models.PositiveSmallIntegerField(default=0,blank=False)
    capacidad_g= models.FloatField(default=0,blank=False)
    cilindraje= models.IntegerField(default=0,blank=False)
    version= models.TextField(default='',blank=False)
    color= models.TextField(default='',blank=False)
    precio= models.DecimalField(default=0, max_digits=10, decimal_places=2, blank =False)
