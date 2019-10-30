from django.shortcuts import render

from .models import Empleado, Productividad, Area, Contrato
from django.shortcuts import redirect
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EmpleadoSerializer, ProductividadSerializer, AreaSerializer, ContratoSerializer

# Create your views here.
def nuevo_empleado(request):
   empleado = Empleado.object.all()
   return render(request,'empleados.html',{'empleados':empleado})

class EmpleadoView(ModelViewSet):
   queryset = Empleado.objects.all().order_by('id')
   serializer_class = EmpleadoSerializer

class AreaView(ModelViewSet):
   queryset = Area.objects.all().order_by('id')
   serializer_class = AreaSerializer


class ProductividadView(ModelViewSet):
   queryset = Productividad.objects.all().order_by('id')
   serializer_class = ProductividadSerializer

class ProductividadEmpleado(APIView):
   def get(self, request, id=None):
      usuario = [Productividad.objects.filter(id_empleado=id).order_by('-fecha').values('fecha','cantidad')]
      return Response(usuario)
   
   #guardar una imagen con los datos en la matplotlib