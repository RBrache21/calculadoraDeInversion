from django.contrib import admin
from .models import  Producto, Inversion, User, Feriado

admin.site.register(Producto)
admin.site.register(Inversion)
admin.site.register(User)
admin.site.register(Feriado)