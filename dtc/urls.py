
from django.contrib import admin
from django.urls import path,include

"""manggil file  views """
from . import views


urlpatterns = [
    # Halaman List
    path('', views.dtc, name='dtc'),

    path('prediksidtc', views.prediksidtc, name='prediksidtc'),

    path('prediksidtc2', views.prediksidtc2, name='prediksidtc2'),

    # Menghapus
    path('hapus/<delete_id>', views.hapus, name='hapus'),

    path('resultdtc', views.resultdtc, name='resultdtc'),

    # Ekport Csv
    path('export_csv/', views.export_csv, name='export_csv'),

    # Ekport Excel
    path('export_xls/', views.export_xls, name='export_xls'),
]
