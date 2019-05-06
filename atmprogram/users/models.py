# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Atmdb(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    adrress=models.CharField(max_length=50)
    phoneno=models.IntegerField()
    atmno=models.IntegerField()
    balance=models.IntegerField()
    photo=models.CharField(max_length=50)
class Meta:
    db_table='atmdatabase'