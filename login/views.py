from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            
            return redirect("/")
            print("Logged in successfully")
        
    else:
        return render(request,'login.html')
        
def logout(request):
    auth.logout(request)
    
    return redirect("/")
    
    
