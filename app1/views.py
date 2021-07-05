from django.contrib import auth
from django.http.response import HttpResponseRedirect
from app1.forms import signinform, signupform,createblogform
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import pchangeform, presetform
from django.contrib.auth.decorators import login_required
from .models import blog
from django.views import View




# Create your views here.
def home(request):
    return render(request,'home.html')



# for signup ...................
def signup(request):
    if request.method=='POST':
        fm=signupform(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request,'user allready exist ......')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email id is allready in used... try with diffrernt email id')
        else :
            if fm.is_valid():
                fm.save()
                messages.info(request,'user successfully added .........now you can login to your account')
            else:
                messages.error(request,'sorry some data are not in proper format....')
    form1=signupform
    form2=signinform
    return render(request,'auth.html',{'form1':form1,'form2':form2})




# for signin of user...................
def signin(request):
    if request.method=='POST':
        fm=signinform(request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['username']
            ps=fm.cleaned_data['password']
            x=authenticate(username=un,password=ps)
            if x is not None:
                login(request,x)
                return HttpResponseRedirect('/profile/')
            else:
                messages.error(request,'sorry username or password is incorrect...')
    form1 = signupform
    form2 = signinform
    return render(request, 'auth.html', {'form1': form1, 'form2': form2})


# for profile page...........
@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

# for password change ...........
@login_required
def pchange(request):
    if request.method=='POST':
        fm=pchangeform(data=request.POST,user=request.user)
        if fm.is_valid():
            fm.save()
            messages.info(request,'successfully password changed........')
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'sorry entered data is not in proper format')
            return render(request, 'pchange.html', {'form': fm})
    else:
        fm=pchangeform(user=request.user)
        return render(request,'pchange.html',{'form':fm})


# for creating blog..................
@login_required
def createblog(request):
    form=createblogform
    if request.method=='POST':
        fm=createblogform(request.POST,request.FILES)
        if fm.is_valid():
            print('................success 1')
            t=fm.cleaned_data['title']
            c=fm.cleaned_data['content']
            p=fm.cleaned_data['photo']
            u=request.user
            obj=blog(user=u,title=t,content=c,photo=p)
            obj.save()
            messages.info(request,'blog created successfully........')
            update_session_auth_hash(request,obj.user)
            # return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'some data is incorrect')
            # return render(request,'createblog.html',{'form':form})
    return render(request, 'createblog.html', {'form': form})


