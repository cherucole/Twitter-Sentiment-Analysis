# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 09:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('twitter', '0004_auto_20181104_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AlterField(
            model_name='sentimentstwitterhashtag',
            name='negative_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sentimentstwitterhashtag',
            name='neutral_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sentimentstwitterhashtag',
            name='postive_count',
            field=models.IntegerField(),
        ),
    ]