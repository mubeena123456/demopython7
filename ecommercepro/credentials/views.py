from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already used")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('credentials:login')

        else:
            messages.info(request,"password doesn't match")
            return redirect('credentials:register')


    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('shop:allProdCat')
        else:
            messages.info(request,"invalid username or password")
            return redirect('credentials:login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('credentials:home')