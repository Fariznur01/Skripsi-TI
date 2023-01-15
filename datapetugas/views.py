from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from .forms import SignUpForm


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def datapetugas(request):
    User = get_user_model()
    semua_petugas = User.objects.all()
    context = {
        'page_title': 'Data Petugas',
        'semua_petugas': semua_petugas,
    }
    return render(request, 'datapetugas/datapetugas.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambah02(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
            messages.success(request, "Akun Berhasil di Buat")
            if new_user is not None:
                login(request, new_user)
                return redirect('datapetugas:datapetugas')
        else:
            messages.error(request, "Akun Gagal di Buat karena password berbeda atau password terlalu sederhana")
            form = SignUpForm()
    form = SignUpForm()
    context = {
        "form": form,
        'page_title': 'Tambah Petugas',
    }
    return render(request, "datapetugas/tambah02.html", context)

@login_required(login_url=settings.LOGIN_URL)
def hapus(request, delete_id):
    User = get_user_model()
    User.objects.filter(id=delete_id).delete()
    messages.info(request, "Akun Berhasil di Hapus")
    return redirect('datapetugas:datapetugas')

