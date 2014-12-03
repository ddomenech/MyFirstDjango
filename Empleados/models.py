from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Puesto(models.Model):
	nombre_puesto = models.TextField(max_length=200)
	user = models.ForeignKey(User, blank = True, null = True,	related_name='puestos')


	def __str__(self):
		return self.nombre_puesto
	def __unicode__(self):
		return '%d: %s' % (self.id, self.nombre_puesto)

class Empleado(models.Model):
	nombre_empleado = models.TextField(max_length=200)
	Apellidos_empleado = models.TextField(max_length=200)
	Salario_empleado = models.DecimalField(max_digits=15, decimal_places=2)
	Activo_empleado = models.BooleanField(default=True)
	Fecha_empleado = models.DateTimeField('Fecha Empleado')
	puesto = models.ForeignKey(Puesto, null=True)
	user = models.ForeignKey(User, blank = True, null = True,	related_name='empleados')

	def __str__(self):
		return self.nombre_empleado +' ' + self.Apellidos_empleado
	class Meta:
		ordering = ['-Fecha_empleado']
# class Tareas_Empleado(models.Model):
# 	empleado = models.ForeignKey(Empleado)
# 	tarea = models.ForeignKey(Empleado)

class Tareas(models.Model):
	nombre_tarea = models.TextField(max_length=200)
	descripcion_tarea = models.TextField(max_length=2000)
	prioridad_tarea = models.IntegerField()
	empleados = models.ManyToManyField(Empleado, verbose_name='list of tareas')
	user = models.ForeignKey(User, blank = True, null = True,	related_name='tareas')
	def __str__(self):
		return self.nombre_tarea
