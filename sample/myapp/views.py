# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Dbcon
# Create your views here.
def show(request):
    return HttpResponse('hello')
def htmlshow(request):
    return render(request,'sample.html',{})
def html2show(request):
    return render(request,'html2.html',{'first':1,'sss':['a','b','c']})
def insertdb(request):
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']
        obb=Dbcon(name=name,age=age)
        obb.save()
        # return render(request,'html3.html',{'first':name,'sss':['a','b','c']})
        return redirect(dbshow)
def dbshow(request):
    obj=Dbcon.objects.all()
    # insert=''
    # for i in obj:
    #     insert+="name:"+i.name+'age:'+str(i.age)
    # return HttpResponse(insert)
    return render(request,'html3.html',{'first':obj})
def dbupdate(request):
    obj=Dbcon.objects.all()
    for i in obj:
        if i.name=='meghal':
            i.name='godson'
            i.save()
    return redirect(dbshow)
def dbdelete(request):
    obj=Dbcon.objects.all()
    for i in obj:
        if i.name=='sarun':
            i.delete()
    return redirect(dbshow)
def dbget(request):
    obj=Dbcon.objects.get(name='aju')
    return render(request,'html3.html',{'third':obj})