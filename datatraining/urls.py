
from django.contrib import admin
from django.urls import path,include

"""manggil file  views """
from . import views


urlpatterns = [
    # Halaman List
    path('', views.datatraining, name='datatraining'),

    #Halaman upload
    path('uploadtraining/', views.uploadtraining, name='uploadtraining'),

    #Hapus data
    path('hapus_file/<int:pk>/', views.hapus_file, name='hapus_file'),

]
