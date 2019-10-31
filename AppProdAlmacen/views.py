from django.shortcuts import render

from .models import Empleado, Productividad, Area, Contrato
from django.shortcuts import redirect
from django.utils import timezone

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EmpleadoSerializer, ProductividadSerializer, AreaSerializer, ContratoSerializer

import plotly.offline as opy
import plotly.graph_objects as go
from django.views.generic import TemplateView

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
      usuarios = Productividad.objects.filter(id_empleado=id).order_by('-fecha').values('fecha','cantidad')
      fechas  = []
      cantidades = []
      for user in usuarios:
         print(user)
         fechas.append(user["fecha"])
         cantidades.append(user["cantidad"])
      return Response({'fechas': fechas, 'cantidades': cantidades})


   

class Graph(TemplateView):
   pagina = 'index.html'

   def get_context_data(self, **kwargs):
      context = super(Graph, self).get_context_data(**kwargs)

      
      datos = [go.Bar(y=[200,100,300,400,600,256,343])]
      titulo_grafico = "Grafica de prueba"

      grafica_en_div = plotly.offline.plot(grafica, auto_open=False, output_type="div")

      context['index'] = div
      return context




