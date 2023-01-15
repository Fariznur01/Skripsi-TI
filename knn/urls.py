
from django.contrib import admin
from django.urls import path,include

"""manggil file  views """
from . import views


urlpatterns = [
    # Halaman List
    path('', views.knn, name='knn'),

    path('prediksiknn', views.prediksiknn, name='prediksiknn'),

    path('prediksiknn2', views.prediksiknn2, name='prediksiknn2'),

    # Menghapus
    path('hapus/<delete_id>', views.hapus, name='hapus'),

    path('result', views.result, name='result'),

    # Ekport Csv
    path('export_csv/', views.export_csv, name='export_csv'),

    # Ekport Excel
    path('export_xls/', views.export_xls, name='export_xls'),

]
