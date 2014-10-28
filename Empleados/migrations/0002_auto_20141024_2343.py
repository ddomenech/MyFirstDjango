# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre_tarea', models.TextField(max_length=200)),
                ('descripcion_tarea', models.TextField(max_length=2000)),
                ('prioridad_tarea', models.IntegerField()),
                ('empleados', models.ManyToManyField(to='Empleados.Empleado', related_name='tareas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='empleado',
            name='Fecha_empleado',
            field=models.DateTimeField(default=datetime.date(2014, 10, 24), verbose_name='Fecha Empleado'),
            preserve_default=False,
        ),
    ]
