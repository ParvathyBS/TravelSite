from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# from .models import Background


# Create your views here.
def register(request):
    # b = Background.objects.all()
    if request.method == 'POST':
        u = request.POST['username']
        f = request.POST['first_name']
        la = request.POST['last_name']
        e = request.POST['email']
        p = request.POST['password']
        cp = request.POST['cpassword']

        if p == cp:
            if User.objects.filter(username=u).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=e).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=u, first_name=f, last_name=la, email=e, password=p)
                user.save()
                return redirect('login')
        else:
            messages.info("PASSWORD NOT MATCHING")
            return redirect('register')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "INVALID CREDENTIALS")
            return redirect('login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
