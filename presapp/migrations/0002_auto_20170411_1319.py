# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-11 07:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='rdate',
            field=models.DateTimeField(blank=True, db_column='rDate', default=datetime.datetime(2017, 4, 11, 13, 19, 43, 557929), null=True),
        ),
        migrations.AlterField(
            model_name='presciptiontemplates',
            name='savedate',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 11, 13, 19, 43, 559929)),
        ),
    ]