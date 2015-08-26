# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanternapp', '0003_auto_20150821_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('color', models.CharField(max_length=50)),
                ('flipper', models.ForeignKey(to='lanternapp.Flipper')),
            ],
        ),
    ]
