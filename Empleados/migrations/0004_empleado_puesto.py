# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0003_auto_20141123_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(to='Empleados.Puesto', null=True),
            preserve_default=True,
        ),
    ]
