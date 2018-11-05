# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-04 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentsTwitterHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=128)),
                ('sample_size', models.CharField(max_length=100)),
                ('postive_count', models.CharField(max_length=100)),
                ('neutral_count', models.CharField(max_length=100)),
                ('negative_count', models.CharField(max_length=100)),
                ('negative_tweets', models.CharField(max_length=100)),
                ('neutral_tweets', models.CharField(max_length=100)),
                ('postive_tweets', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Sentiments',
        ),
    ]