from django.urls import path

"""manggil file  views """
from . import views

urlpatterns = [

    # Bagiam Pasien
    # Menambah
    path('tambah/', views.tambah, name='tambah'),

    # Menghapus
    path('hapus/<delete_id>', views.hapus, name='hapus'),

    # Mengupdate
    path('update/<update_id>', views.update, name='update'),

    # Halaman List
    path('', views.datapasien, name='datapasien'),

    # Ekport Csv
    path('export_csv/', views.export_csv, name='export_csv'),

    # Ekport Excel
    path('export_xls/', views.export_xls, name='export_xls'),
]
