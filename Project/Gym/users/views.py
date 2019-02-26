from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from  . forms import  UserRegister
# from . forms import  ProfileUpdateForm
from django.http import request
from django.contrib.messages import success
from django.contrib.auth.decorators import login_required


# from django.core import mail
# from django.test import TestCase



def signup(request):
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
        	form.save()
        	username=form.cleaned_data.get('username')
        	success(request,f'Account created  for {username}!. You able to Login')
        	return redirect('login')
    else:
        form=UserRegister()
    return render(request,'users/register.html',{'form':form})

# @login_required
# def profile(request):
# 	if request.method=='POST':
# 		u_form=UserUpdateForm(request.POST,instance=request.user)
# 		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
# 		if u_form.is_valid and p_form.is_valid :
# 			u_form.save()
# 			p_form.save()
# 			success(request,f'Account has been updated ')
# 			return redirect('profile')
# 	else:
# 		u_form=UserUpdateForm(instance=request.user)
# 		p_form=ProfileUpdateForm(instance=request.user.profile)

# 	context={
# 	'u_form':u_form,
# 	'p_form':p_form,
# 	}
# 	return render(request,'users/profile.html',context)