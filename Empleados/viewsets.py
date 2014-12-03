from .models import Empleado, Puesto, Tareas
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmpleadoSerializer, PuestoSerializer, TareasSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets
from .. import permissions, authenticators

class EmpleadoViewSet(viewsets.ModelViewSet):
	queryset = Empleado.objects.all()
	model = Empleado
	serializer_class = EmpleadoSerializer
	permission_classes = (permissions.IsOwner,)

	def pre_save(self, obj):
		#add user to object if user is logged in
		if isinstance(self.request.user, User):
			obj.user = self.request.user

class PuestoViewSet(viewsets.ModelViewSet):
	queryset = Puesto.objects.all()
	model = Puesto
	serializer_class = PuestoSerializer
	permission_classes = (permissions.IsOwner,)

class TareasViewSet(viewsets.ModelViewSet):
	queryset = Tareas.objects.all()
	serializer_class = TareasSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	model = User
	serializer_class = UserSerializer

	def get_permissions(self):
		#Allow non-authenticated user to create
		return (AllowAny() if self.request.method == 'POST'
			else permissions.IsStaffOrTargetUser()),


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class AuthView(APIView):
	authentication_classes = (authenticators.QuietBasicAuthentication,)

	def post(self, request, *args, **kwargs):
		login(request, request.user)
		return Response(serializers.UserSerializer(request.user).data)

	def delete(self, request, *args, **kwargs):
		logout(request)
		return Response()
