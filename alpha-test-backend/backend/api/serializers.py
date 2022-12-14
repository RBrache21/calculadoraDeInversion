from rest_framework import serializers
from .models import Producto, Inversion, User, Feriado

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'cantidadDiasHoraOperativa', 'cantidadDiasHoraNoOperativa', 'cantidadDiasHoraOperativaReinversion', 'cantidadDiasHoraNoOperativaReinversion')

class InversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversion
        fields = ('id', 'producto', 'enReinversion', 'plazo', 'fechaCreacion')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
      
class FeriadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feriado
        fields = ('id', 'fecha')