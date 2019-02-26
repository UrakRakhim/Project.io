from django.shortcuts import render
from django.http  import HttpResponse,request

def Main(request):
	return render(request,'Gym_Main/base.html')

# Create your views here.
