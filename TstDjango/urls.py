from django.conf.urls import patterns, include, url
from Empleados.models import Empleado, Tareas, Puesto
from django.contrib import admin
import pytz

class PuestoInline(admin.TabularInline):
	model = Puesto
	extra = 3

class TareasInline(admin.TabularInline):
	model = Tareas.empleados.through
	extra = 4

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('__str__','Fecha_empleado', 'Activo_empleado')
	fieldsets = [
	('Fecha Informacion', {'fields': ['Fecha_empleado']}),
	('Datos Salario', {'fields': ['Salario_empleado']}),
	('Datos Empleado', {'fields': ['nombre_empleado', 'Apellidos_empleado', 'Activo_empleado']}),
	]
	#('Datos Empleado', {'fields': ['Apellidos_empleado', 'nombre_empleado']}),
	inlines = [PuestoInline, TareasInline]
	list_filter = ['Fecha_empleado']
	search_fields = ['Apellidos_empleado']
	date_hierarchy = 'Fecha_empleado'

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Tareas)
admin.site.register(Puesto)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TstDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
