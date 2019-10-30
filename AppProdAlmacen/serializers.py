from .models import Empleado, Contrato, Productividad, Area
from rest_framework import serializers

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
   tipo_contrato = serializers.StringRelatedField(many=False)
   area = serializers.StringRelatedField(many=False)
   class Meta:
      model=Empleado
      fields =('id','nombre_empleado','a_paterno','a_materno', 'edad', 'tipo_contrato', 'area', 'genero')
      
class ContratoSerializer(serializers.HyperlinkedModelSerializer):
   tipo_contrato = serializers.StringRelatedField()
   class Meta:
      model = Contrato
      fields =('nombre_contrato')

class ProductividadSerializer(serializers.HyperlinkedModelSerializer):
   id_empleado = serializers.StringRelatedField(many=False)
   class Meta:
      model = Productividad
      fields =('fecha','cantidad','id_empleado')

class AreaSerializer(serializers.HyperlinkedModelSerializer):
   empleados = serializers.StringRelatedField(many=True)
   class Meta:
      model = Area
      fields = ('id','nombre_area','prod_min','prod_max','empleados')