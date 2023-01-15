from django.urls import path

"""manggil file  views """
from . import views


urlpatterns = [
    #Halaman List
    path('', views.datapetugas, name='datapetugas'),

    #Menambah
    path('tambah02/', views.tambah02, name='tambah02'),

    #Menghapus
    path('hapus/<delete_id>', views.hapus, name='hapus'),

]
