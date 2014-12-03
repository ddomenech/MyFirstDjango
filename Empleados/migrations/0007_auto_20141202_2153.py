# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Empleados', '0006_empleado_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='user',
            field=models.ForeignKey(related_name='puestos', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tareas',
            name='user',
            field=models.ForeignKey(related_name='tareas', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
