# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse,HttpResponse
from users.models import Atmdb
usern=''
passw=''
# Create your views here.
def getfunc(request,username,password):
    global usern,passw
    usern=username
    passw=password
    return render(request,'userpage.html',{'username':usern,'password':passw})
    # return redirect(indexpage)
def indexpage(request):
    obj=Atmdb.objects.all()
    passw=''
    # for i in obj:
    #     if i.username==username and i.password==password:
    if request.session.has_key('username'):
        usern=request.session['username']
        passw=request.session['password']
        return render(request,'homeuser.html',{'username':usern})
def display(request):
    obj=Atmdb.objects.all()
    # return HttpResponse(obj)
    return render(request,'display.html',{'first':obj})
def updateform(request):
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        atm=request.POST['atm']
        Atmdb.objects.filter(username=request.session['username']).update(name=name,adrress=address,phoneno=phone,atmno=atm)
        return HttpResponse(name+address+phone+atm)
def logout(request):
    del request.session['username']
    return redirect(reverse('login'))
def getajax(request):
    name="success"
    return HttpResponse(name)
def myname(request):
        name="ok"
        return HttpResponse(name)