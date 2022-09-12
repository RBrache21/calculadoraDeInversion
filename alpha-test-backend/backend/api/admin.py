from django.contrib import admin
from .models import  Producto, Inversion, User

admin.site.register(Producto)
admin.site.register(Inversion)
admin.site.register(User)