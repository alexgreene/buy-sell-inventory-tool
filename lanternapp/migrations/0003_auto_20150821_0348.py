# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanternapp', '0002_auto_20150809_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('primary_color', models.CharField(max_length=10)),
                ('secondary_color', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='flipper',
            name='app_title',
            field=models.CharField(default=b'Flipper App', max_length=75),
        ),
        migrations.AddField(
            model_name='flipper',
            name='app_theme',
            field=models.ForeignKey(default=1, to='lanternapp.Theme'),
        ),
    ]
