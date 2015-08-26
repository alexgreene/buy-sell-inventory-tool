# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanternapp', '0004_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='flipper',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='category',
            field=models.ForeignKey(default=1, to='lanternapp.Category'),
        ),
    ]
