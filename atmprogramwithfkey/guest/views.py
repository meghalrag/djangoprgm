# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,reverse
from users.views import *
from users import urls
from forms import regform,loginform
from users.models import logintable,registertable
# Create your views here.
def indexpage(request):
    return render(request,'index.html',{})
def registration(request):
    return render(request,'reg.html',{})
def login(request):
    return render(request,'login.html',{})
def formreg(request):
    if request.method == 'POST':
        form=loginform(request.POST)
        if form.is_valid():   
                # email = formreg.cleaned_data['emailid']
                email=request.POST['email']
                username = form.cleaned_data['username']
                passw=request.POST['password']
                cpass=request.POST['cpassword']
                if passw==cpass:
                        obj=logintable(username=username,password=passw)
                        obj.save()
                        obj=logintable.objects.get(username=username)
                        form.instance.logintable = obj
                        obj1=registertable(emailid=email,fkidreg=form.instance.logintable)
                        obj1.save()
                        return render(request,'regok.html',{'usern':username})
                else:
                        return HttpResponse('password not match')
        else:
                return render(request,'reg.html',{})
def formlogin(request):
    flag=0
    obj=logintable.objects.all()
    if request.method == 'POST':
        username=request.POST['username']
        passw=request.POST['password']
        for i in obj:
            if i.username==username and i.password==passw:
                global usernameg,passwordg
                userid=i.id
                usernameg=i.username
                passwordg=passw
                request.session['username'] = username
                request.session['password'] = passw
                request.session['id'] = userid
                return redirect(reverse('home'))
        return render(request,'login.html',{'msg':'username or password incorrect'})

