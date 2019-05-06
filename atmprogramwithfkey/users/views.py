# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse,HttpResponse
from users.models import *
from forms import Profileform

usern=''
passw=''
# Create your views here.
def indexpage(request):
    if request.session.has_key('id'):
        usern=request.session['username']
        passw=request.session['password']
        obj=registertable.objects.get(fkidreg=request.session['id'])
        if obj.profilepic=='':
                return render(request,'homeuser.html',{'username':obj.profilepic,'id':request.session['id']})
        else:

                stringn='media/'+str(obj.profilepic)
                return render(request,'homeuser.html',{'obj':obj,'username':usern,'id':request.session['id']})
    else:
        return HttpResponse('you are already logged out')
def display(request):
        if request.session.has_key('id'):
                obj=logintable.objects.all()
                lis=[]
                objjoin = registertable.objects.all()
                objjoin2=balancetable.objects.all()
                for i in objjoin2:
                        lis.append(i.balance)
                return render(request,'display.html',{'first':objjoin,'second':lis})
        else:
                 return HttpResponse('you are already logged out')
def updateform(request):
        if request.session.has_key('id'):
                obj=registertable.objects.get(fkidreg=request.session['id'])
                if obj.name==None:

                        count=0
                        accno=1000
                        obj=registertable.objects.all()
                        for i in obj:
                                count+=1
                        accno=accno+count
                        if request.method == 'POST':
                                name=request.POST['name']
                                address=request.POST['address']
                                phone=request.POST['phone']
                                atm=request.POST['atm']
                                registertable.objects.filter(fkidreg=request.session['id']).update(accno=accno,name=name,address=address,phoneno=phone,atmno=atm)
                                return render(request,'message.html',{'username':request.session['username'],'msg':'update successfully'})
                else:
                        return HttpResponse('already updated')
        else:
                return HttpResponse('you are already logged out')
def logout(request):
    del request.session['username']
    del request.session['id']
    del request.session['password']
    return redirect(reverse('login'))

def profileadd(request):
        if request.method=='POST':
                form=Profileform(request.POST, request.FILES)
                if form.is_valid():  
                        proname=form.cleaned_data["picname"]
                        obj=registertable.objects.get(fkidreg=request.session['id'])
                        obj.profilepic=proname
                        obj.save()
                        return render(request,'message.html',{'username':request.session['username'],'msg':'update successfully'})
                else:
                        return render(request,'message.html',{'username':request.session['username'],'msg1':'update failed'})
