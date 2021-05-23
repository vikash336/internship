from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from advnetwork import models
from django.contrib import messages
from django.contrib.auth.models import User
from  advnetwork.forms import newadviser
def con(request):
    data={}
    if request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password'];
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/advnetwork/newadv/')
        else:
            data['error']="Username or password is incorrect"
            res=render(request,'admin.html',data)
            return res

    else:
        return render(request,'admin.html',data)
def vik(request):
    data={}
    if request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password'];
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/advnetwork/view/')
        else:
            data['error']="Username or password is incorrect"
            res=render(request,'login.html',data)
            return res

    else:
        return render(request,'login.html',data)

def siggn(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST.get('email')
        password=request.POST['password']

        # create username
        myuser=User.objects.create_user(username, email, password)
        # myuser.first_name=fname
        # myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been created")
        return redirect('advnetwork/combine')
    else:
        return  HttpResponse('404- not found')
def tstsign(request):
    s="This is Signup Page"
    data={'s':s}
    return render(request,'signup.html',context=data)
def tstlogin(request):
    s="This is Login Page"
    data={'s':s}
    return render(request,'login.html',context=data)
def main(request):
    return render(request,'start.html')
def combine(request):
    s="Enter your choice"
    data={'s':s}
    return render(request,'combine.html',context=data)
def gusain(request):
    return render(request,'admin.html')

def inuser(request):
    s="Confirm Yourself"
    data={'s':s}
    return render(request,'user.html',context=data)
def newadv(request):
    form=newadviser()
    return render(request,'addadv.html',{'form':form})


def tst(request):
    s="this is test "
    return HttpResponse(s)

def add(request):
    if request.method=='POST':
        form=newadviser(request.POST)
        adv=models.adviser()
        adv.adname=form.data['adname']
        adv.ad_id=form.data['ad_id']
        adv.bookingtime=form.data['bookingtime']
        adv.bookid=form.data['bookid']
        adv.save()
    s="Record Stored<br>"
    return HttpResponse(s)
def view(request):
    advis=models.adviser.objects.all()
    res=render(request,'view.html',{'advis':advis})
    return res
