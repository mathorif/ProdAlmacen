from django.contrib import admin

from .models import Empleado, Contrato, Productividad, Area 

# Register your models here.
admin.site.register([Empleado,Contrato,Productividad,Area ])
