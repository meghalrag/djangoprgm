# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-25 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atmdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('adrress', models.CharField(max_length=50)),
                ('phoneno', models.IntegerField()),
                ('atmno', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('photo', models.CharField(max_length=50)),
            ],
        ),
    ]
