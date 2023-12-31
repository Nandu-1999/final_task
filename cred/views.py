from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken Already')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password=password)
                user.save()

                print("User registration completed..!!)")
                return redirect('login')
        else:
            messages.info(request,"Password are not matched")
            return redirect('register')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def form(request):
    return render(request,'form.html')