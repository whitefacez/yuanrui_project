# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0002_auto_20171031_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakdownResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BDRName', models.CharField(max_length=20)),
                ('BDRRemarks', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='breakdownlogin',
            name='Result',
            field=models.CharField(max_length=20),
        ),
    ]
