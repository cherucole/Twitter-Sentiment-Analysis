# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-04 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20181104_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentimentstwitterhashtag',
            name='negative_count',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sentimentstwitterhashtag',
            name='neutral_count',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sentimentstwitterhashtag',
            name='postive_count',
            field=models.IntegerField(max_length=100),
        ),
    ]