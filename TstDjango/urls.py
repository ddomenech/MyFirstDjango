from django.conf.urls import patterns, include, url
from Empleados.models import Empleado, Tareas, Puesto
from django.contrib import admin
import pytz
admin.autodiscover()

# class PuestoInline(admin.TabularInline):
# 	model = Puesto
# 	extra = 2

# class TareasInline(admin.TabularInline):
# 	model = Tareas.empleados.through
# 	extra = 2

# class EmpleadoAdmin(admin.ModelAdmin):
# 	list_display = ('__str__','Fecha_empleado', 'Activo_empleado')
# 	fieldsets = [
# 	('Fecha Informacion', {'fields': ['Fecha_empleado']}),
# 	('Datos Salario', {'fields': ['Salario_empleado']}),
# 	('Datos Empleado', {'fields': ['nombre_empleado', 'Apellidos_empleado', 'Activo_empleado']}),
# 	]
# 	#('Datos Empleado', {'fields': ['Apellidos_empleado', 'nombre_empleado']}),
# 	inlines = [PuestoInline, TareasInline]
# 	list_filter = ['Fecha_empleado']
# 	search_fields = ['Apellidos_empleado']
# 	date_hierarchy = 'Fecha_empleado'

# admin.site.register(Empleado)
# admin.site.register(Tareas)
# admin.site.register(Puesto)

from Empleados.api.viewsets import EmpleadoViewSet, PuestoViewSet, TareasViewSet, UserViewSet, GroupViewSet, AuthView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
router.register(r'puestos', PuestoViewSet)
router.register(r'tareas', TareasViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('Empleados.empleados',
	url(r'^', include(router.urls)),
	url(r'^api/auth/$', AuthView.as_view(), name='authenticate'),
    url(r'^admin/', include(admin.site.urls)),
)
