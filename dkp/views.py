from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Selamat Datang" )
            return redirect('dashboard')
        else:
            # messages.success(request, ("There Was An Error Logging In, Try Again..."))
            messages.error(request, "Gagal Login Password atau Username Salah")
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html', {})


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    context = {
        'page_title': 'Dashboard'
    }
    return render(request, "dashboard.html", context)

@login_required(login_url=settings.LOGIN_URL)
def logout_user(request):
    logout(request)
    messages.success(request, "Berhasil Log Out")
    # messages.success(request, ("You Were Logged Out!"))
    return redirect('login_user')
