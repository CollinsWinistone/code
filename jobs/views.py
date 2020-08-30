from django.shortcuts import render
from django.http import HttpResponse
from . models import Job,Qualification,Description,Profile
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    
    jobs = Job.objects.all()
    users = User.objects.all()
    qual =Qualification.objects.all()
    
    return render(request,'index.html',{'jobs':jobs,'user':users})


def aboutJob(request,job_id):
    """It gives a detailed instruction about a job instance"""
    current_job =Job.objects.get(id=job_id)
    
    
    return render(request,'aboutjob.html',{'job':current_job})