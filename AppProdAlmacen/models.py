from django.db import models
from django.utils import timezone #requerido para la fecha
from django.conf import settings

class Empleado(models.Model): #la llave primaria es automatica por heredarse del modelo 
   nombre_empleado = models.CharField(max_length=15)
   a_paterno = models.CharField(max_length=15)
   a_materno = models.CharField(max_length=15)
   edad = models.IntegerField()
   tipo_contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, null = False) #llave foranea uno a uno
   area= models.ForeignKey('Area',on_delete=models.CASCADE, related_name='empleados',null = False) #llave foranea uno a muchos
   opciones_genero = [('MASC', 'Masculino'),('FEME', 'Femenino'),]
   genero=models.CharField(max_length=4,choices=opciones_genero,)
   
   def __str__(self):
      return '{},{},{}'.format(self.nombre_empleado,self.a_paterno,self.a_materno)

class Contrato(models.Model):
   nombre_contrato = models.CharField(max_length=15)

   def __str__(self):
      return self.nombre_contrato

class Productividad(models.Model):
   id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, null = False) #llave foranea
   fecha = models.DateTimeField(default=timezone.now)
   cantidad = models.IntegerField()

   def __str__(self):
      return '{} -- {} -- {}'.format(self.id_empleado,self.cantidad,self.fecha.strftime("%d/%m/%y"))

class Area(models.Model):
   nombre_area = models.CharField(max_length=15)
   prod_min = models.IntegerField()
   prod_max = models.IntegerField()

   def __str__(self):
      return self.nombre_area