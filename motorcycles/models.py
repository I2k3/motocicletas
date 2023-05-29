from django.conf import settings
# ...code
from django.db import models

# Create your models here 

class Motocicleta(models.Model):

    description = models.TextField(blank=True)
    marca = models.TextField(default='',blank=False)
    modelo = models.TextField(default='',blank=False)
    motor = models.TextField(default='',blank=False)
    consumog= models.PositiveSmallIntegerField(default=0,blank=False)
    capacidadg= models.FloatField(default=0,blank=False)
    cilindraje= models.IntegerField(default=0,blank=False)
    version= models.TextField(default='',blank=False)
    color= models.TextField(default='',blank=False)
    precio= models.DecimalField(default=0, max_digits=10, decimal_places=2, blank =False)

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    motocicleta = models.ForeignKey('motorcycles.Motocicleta', related_name='motocicleta', on_delete=models.CASCADE)