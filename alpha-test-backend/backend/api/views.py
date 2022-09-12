import datetime
from rest_framework import viewsets
from backend.api.serializers import ProductoSerializer, InversionSerializer, UserSerializer, FeriadoSerializer
from .models import Producto, Inversion, User, Feriado
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InversionViewSet(viewsets.ModelViewSet):
    queryset = Inversion.objects.all()
    serializer_class = InversionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FeriadoViewSet(viewsets.ModelViewSet):
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer

@api_view(['POST'])
def crearInversion(request):
    producto = Producto.objects.get(id=request.data['producto'])
    inversion = Inversion(producto=producto, enReinversion=request.data['enReinversion'], plazo=request.data['plazo'])
    inversion.save()

    hora_laborable = datetime.time(10, 30, 0)

    inversion.fechaCreacion = inversion.fechaCreacion.astimezone(datetime.timezone(datetime.timedelta(hours=-4)))
 
    
    fechaInicio = inversion.fechaCreacion
    if inversion.fechaCreacion.time() < hora_laborable:
        if inversion.enReinversion:
            fechaInicio = fechaInicio + datetime.timedelta(days=producto.cantidadDiasHoraOperativaReinversion)
        else:
            fechaInicio = inversion.fechaCreacion + datetime.timedelta(days=producto.cantidadDiasHoraOperativa)

        while fechaInicio.weekday() > 4:
            fechaInicio = fechaInicio + datetime.timedelta(days=1)

    else:
        if inversion.enReinversion:
            fechaInicio = fechaInicio + datetime.timedelta(days=producto.cantidadDiasHoraNoOperativaReinversion)
        else:
            fechaInicio = fechaInicio + datetime.timedelta(days=producto.cantidadDiasHoraNoOperativa)
        
        while fechaInicio.weekday() > 4:
            fechaInicio = fechaInicio + datetime.timedelta(days=1)
    

    fechaFin = fechaInicio + datetime.timedelta(days=inversion.plazo)
    while fechaFin.weekday() > 4:
        fechaFin = fechaFin + datetime.timedelta(days=1)
    
    plazoReal = (fechaFin - fechaInicio).days
    
    return Response({
        'producto': producto.id,
        'plazo' : inversion.plazo,
        'fechaInicio': fechaInicio,
        'fechaFin': fechaFin,
        'plazoReal': plazoReal
    })

@api_view(['POST'])
def login(request):
    try:
        user = User.objects.get(email=request.data['email'])
        if user.password == request.data['password']:
            
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({
                'error': 'Contraseña incorrecta'
            })
    except User.DoesNotExist:
        return Response({
            'error': 'Usuario no encontrado'
        })
    


 

    


    


   
    