from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import views
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        
        
        email = request.POST['email']
        
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        
        print("Data saved and user created successfully...")
        
        return redirect('login')
    
        
        
    else:
        
    
        return render(request,'register.html')
    
    