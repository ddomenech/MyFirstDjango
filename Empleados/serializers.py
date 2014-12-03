from rest_framework import serializers
from .models import Empleado, Puesto, Tareas
from django.contrib.auth.models import User, Group

class EmpleadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empleado
		fields = ('id', 'nombre_empleado', 'Apellidos_empleado', 'Salario_empleado', 'Activo_empleado', 'Fecha_empleado', 'puesto')

class PuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Puesto
		fields = ('id', 'nombre_puesto')

class TareasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tareas
		fields = ('id', 'nombre_tarea', 'descripcion_tarea', 'prioridad_tarea', 'empleados')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')