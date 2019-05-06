# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,reverse
from users.views import indexpage as user
from users.views import getfunc
from users import urls
from users.models import Atmdb
from forms import EmployeeForm
usernameg=''
passwordg=''
# Create your views here.
def indexpage(request):
    return render(request,'index.html',{})
def registration(request):
    return render(request,'reg.html',{})
def login(request):
    return render(request,'login.html',{})
def formreg(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)  
        if form.is_valid():
            obj=Atmdb.objects.all()
            if obj==None:
                id=1
            else:
                count=1
                for i in obj:
                    count+=1
            id=count
            username=request.POST['username']
            passw=request.POST['password']
            cpass=request.POST['cpassword']
            if passw==cpass:
                obb=Atmdb(userid=id,username=username,password=passw,name='nil',adrress='nil',phoneno=0,atmno=0,balance=0,photo='nil')
                obb.save()
                return render(request,'regok.html',{})
            else:
                return HttpResponse('sorry')
        else:
            return render(request,'reg.html',{})
def formlogin(request):
    flag=0
    obj=Atmdb.objects.all()
    if request.method == 'POST':
        username=request.POST['username']
        passw=request.POST['password']
        for i in obj:
            if i.username==username and i.password==passw:
                global usernameg,passwordg
                usernameg=i.username
                passwordg=passw
                request.session['username'] = username
                request.session['password'] = passw
                return redirect(reverse('home'))
        return render(request,'login.html',{'msg':'username or password incorrect'})

