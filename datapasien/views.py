from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from .models import Basis

from .forms import BasisForm

from django.contrib.auth.decorators import login_required

# Ekspor CSV/Excel
from .resource import PasienResource
from django.conf import settings

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def datapasien(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        semua_pasien = Basis.objects.filter(Nama_Pasien__contains=kata_kunci)
        context = {
            'page_title': 'Data Latih',
            'semua_pasien': semua_pasien,
        }
    else:
        semua_pasien = Basis.objects.all()
        context = {
            'page_title': 'Data Latih',
            'semua_pasien': semua_pasien,
        }

    return render(request, 'datapasien/datapasien.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambah(request):
    # model pasien_form
    pasien_form = BasisForm(request.POST or None)
    # metode pengiriman memakai POST
    if request.method == 'POST':
        # Jika Data Valid
        if pasien_form.is_valid():
            # Akan Tesimpan di Database
            pasien_form.save()
            messages.success(request, "Data Berhasil di Tambah")
        return redirect('datapasien:datapasien')
    context = {
        "page_title": "Tambah Data",
        "pasien_form": pasien_form,
    }
    return render(request, 'datapasien/tambah.html', context)

@login_required(login_url=settings.LOGIN_URL)
def update(request, update_id):
    pasien_update = Basis.objects.get(id=update_id)

    data = {
        'Nama_Pasien': pasien_update.Nama_Pasien,
        'Tgl_Periksa': pasien_update.Tgl_Periksa,
        'Radius_mean': pasien_update.Radius_mean,
        'Texture_mean': pasien_update.Texture_mean,
        'Perimeter_mean': pasien_update.Perimeter_mean,
        'Area_mean': pasien_update.Area_mean,
        'Smoothness_mean': pasien_update.Smoothness_mean,
        'Compactness_mean': pasien_update.Compactness_mean,
        'Concavity_mean': pasien_update.Concavity_mean,
        'Concave_points_mean': pasien_update.Concave_points_mean,
        'Symmetry_mean': pasien_update.Symmetry_mean,
        'Fractal_dimension_mean': pasien_update.Fractal_dimension_mean,
        # Se
        'Radius_se': pasien_update.Radius_se,
        'Texture_se': pasien_update.Texture_se,
        'Perimeter_se': pasien_update.Perimeter_se,
        'Area_se': pasien_update.Area_se,
        'Smoothness_se': pasien_update.Smoothness_se,
        'Compactness_se': pasien_update.Compactness_se,
        'Concavity_se': pasien_update.Concavity_se,
        'Concave_points_se': pasien_update.Concave_points_se,
        'Symmetry_se': pasien_update.Symmetry_se,
        'Fractal_dimension_se': pasien_update.Fractal_dimension_se,
        # worst
        'Radius_worst': pasien_update.Radius_worst,
        'Texture_worst': pasien_update.Texture_worst,
        'Perimeter_worst': pasien_update.Perimeter_worst,
        'Area_worst': pasien_update.Area_worst,
        'Smoothness_worst': pasien_update.Smoothness_worst,
        'Compactness_worst': pasien_update.Compactness_worst,
        'Concavity_worst': pasien_update.Concavity_worst,
        'Concave_points_worst': pasien_update.Concave_points_worst,
        'Symmetry_worst': pasien_update.Symmetry_worst,
        'Fractal_dimension_worst': pasien_update.Fractal_dimension_worst,

    }
    pasien_form = BasisForm(request.POST or None, initial=data, instance=pasien_update)
    # metode pengiriman memakai POST
    if request.method == 'POST':
        # Jika Data Valid
        if pasien_form.is_valid():
            # Akan Tesimpan di Database
            pasien_form.save()
            messages.success(request, "Data Berhasil di Update")
        return redirect('datapasien:datapasien')
    context = {
        "page_title": "Update Data",
        "pasien_form": pasien_form,
    }
    return render(request, 'datapasien/tambah.html', context)


def hapus(request, delete_id):
    Basis.objects.filter(id=delete_id).delete()
    messages.success(request, "Data Berhasil di Hapus")
    return redirect('datapasien:datapasien')

@login_required(login_url=settings.LOGIN_URL)
def export_csv(request):
    pasien = PasienResource()
    Data = pasien.export()
    response = HttpResponse(Data.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'
    return response

@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    pasien = PasienResource()
    Data = pasien.export()
    response = HttpResponse(Data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=data.xls'
    return response