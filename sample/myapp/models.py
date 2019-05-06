# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dbcon(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
class Meta:
    db_table='Sampledb'