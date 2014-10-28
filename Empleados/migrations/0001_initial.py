# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre_empleado', models.TextField(max_length=200)),
                ('Apellidos_empleado', models.TextField(max_length=200)),
                ('Salario_empleado', models.DecimalField(max_digits=15, decimal_places=2)),
                ('Activo_empleado', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre_puesto', models.TextField(max_length=200)),
                ('empleado', models.ForeignKey(to='Empleados.Empleado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
