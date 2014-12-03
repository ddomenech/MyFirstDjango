# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0002_auto_20141024_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puesto',
            name='empleado',
        ),
        migrations.AlterField(
            model_name='tareas',
            name='empleados',
            field=models.ManyToManyField(to='Empleados.Empleado', verbose_name=b'list of tareas'),
            preserve_default=True,
        ),
    ]
