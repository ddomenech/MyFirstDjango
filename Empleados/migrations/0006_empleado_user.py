# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Empleados', '0005_auto_20141201_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.ForeignKey(related_name='empleados', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
