from django.contrib import admin
from django.urls import path, include

from  AppProdAlmacen.views import EmpleadoView, AreaView, ProductividadView, ProductividadEmpleado
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empleado',EmpleadoView,base_name='Empleado')
router.register('area',AreaView,base_name='Area')
router.register('productividad',ProductividadView,base_name='Productividad')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('prodempleado/<id>', ProductividadEmpleado.as_view())
]
