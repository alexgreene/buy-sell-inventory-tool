# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flipper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('purchase_price', models.IntegerField(default=0)),
                ('purchase_date', models.DateField(null=True, blank=True)),
                ('purchase_medium', models.CharField(max_length=75, null=True, blank=True)),
                ('additional_expense', models.IntegerField(default=0)),
                ('sale_price', models.IntegerField(default=0)),
                ('sale_date', models.DateField(null=True, blank=True)),
                ('sale_medium', models.CharField(max_length=75, null=True, blank=True)),
                ('flipper', models.ForeignKey(to='lanternapp.Flipper')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lot_title', models.CharField(max_length=100)),
                ('lot_description', models.TextField()),
                ('purchase_price', models.IntegerField()),
                ('purchase_date', models.DateField(null=True, blank=True)),
                ('purchase_medium', models.CharField(max_length=75)),
                ('flipper', models.ForeignKey(to='lanternapp.Flipper')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lot_title', models.CharField(max_length=100)),
                ('lot_description', models.TextField()),
                ('sale_price', models.IntegerField()),
                ('sale_date', models.DateField(null=True, blank=True)),
                ('sale_medium', models.CharField(max_length=75)),
                ('flipper', models.ForeignKey(to='lanternapp.Flipper')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='purchase_lot',
            field=models.ForeignKey(blank=True, to='lanternapp.PurchaseLot', null=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='sale_lot',
            field=models.ForeignKey(blank=True, to='lanternapp.SaleLot', null=True),
        ),
    ]
