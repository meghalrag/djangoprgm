# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-27 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accno', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('emailid', models.EmailField(max_length=254)),
                ('phoneno', models.IntegerField(null=True)),
                ('profilepic', models.CharField(max_length=50, null=True)),
                ('atmno', models.IntegerField(null=True)),
                ('fkidreg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.login')),
            ],
        ),
        migrations.AddField(
            model_name='balance',
            name='fkidbal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.login'),
        ),
    ]
