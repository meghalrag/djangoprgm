# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField( max_length=50,unique=True)
    password=models.CharField( max_length=50)

class registertable(models.Model):
    accno=models.IntegerField(null=True)
    name=models.CharField(max_length=50,null=True)
    address=models.CharField( max_length=50,null=True)
    emailid=models.EmailField( max_length=254)
    phoneno=models.IntegerField(null=True)
    profilepic=models.ImageField(upload_to = 'uploadpic',null=True)
    atmno=models.IntegerField(null=True)
    fkidreg=models.ForeignKey(logintable, on_delete=models.CASCADE)

class balancetable(models.Model):
    balance=models.IntegerField(null=True)
    fkidbal=models.ForeignKey(logintable, on_delete=models.CASCADE)