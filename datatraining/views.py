from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from .models import File
from .forms import FileForm

# Create your views here.
#upload
@login_required(login_url=settings.LOGIN_URL)
def datatraining(request):
    semua_files = File.objects.all()
    context = {
        'page_title': 'Data Training',
        'semua_files': semua_files,
    }
    return render(request, 'datatraining/file.html', context)

@login_required(login_url=settings.LOGIN_URL)
def uploadtraining(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "File Berhasil di Simpan")
            return redirect('datatraining:datatraining')
        else:
            messages.error(request, "File Gagal di Simpan")
            form = FileForm()
    else:
        form = FileForm()
    return render(request, 'datatraining/uploadtraining.html', {
        'form': form
    })
    return render(request, 'datatraining/uploadtraining.html')

@login_required(login_url=settings.LOGIN_URL)
def hapus_file(request, pk):
    if request.method == 'POST':
        excel = File.objects.get(pk=pk)
        excel.delete()
        messages.success(request, "File Berhasil di Hapus")
    return redirect('datatraining:datatraining')

