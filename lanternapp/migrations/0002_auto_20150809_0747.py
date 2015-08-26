# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lanternapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaselot',
            old_name='purchase_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='purchaselot',
            old_name='lot_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='purchaselot',
            old_name='purchase_medium',
            new_name='medium',
        ),
        migrations.RenameField(
            model_name='purchaselot',
            old_name='purchase_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='purchaselot',
            old_name='lot_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='salelot',
            old_name='sale_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='salelot',
            old_name='lot_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='salelot',
            old_name='sale_medium',
            new_name='medium',
        ),
        migrations.RenameField(
            model_name='salelot',
            old_name='sale_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='salelot',
            old_name='lot_title',
            new_name='title',
        ),
    ]
