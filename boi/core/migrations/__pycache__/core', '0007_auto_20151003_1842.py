# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151003_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalprofile',
            name='data_compra',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='peso',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='preco',
            field=models.FloatField(default=0.0),
        ),
    ]
