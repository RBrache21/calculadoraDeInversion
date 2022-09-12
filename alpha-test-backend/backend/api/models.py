from django.db import models
from django.core.validators import  MinValueValidator 



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    cantidadDiasHoraOperativa = models.IntegerField()
    cantidadDiasHoraNoOperativa = models.IntegerField()
    cantidadDiasHoraOperativaReinversion = models.IntegerField()
    cantidadDiasHoraNoOperativaReinversion = models.IntegerField()

class Inversion(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    enReinversion = models.BooleanField()
    plazo = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   