from django.contrib import admin
from django.urls import path,include

"""manggil file  views """
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_user, name="login_user"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('datapasien/',include(('datapasien.urls','datapasien'),namespace='datapasien')),

    path('datapetugas/',include(('datapetugas.urls','datapetugas'),namespace='datapetugas')),

    path('datatraining/', include(('datatraining.urls', 'datatraining'), namespace='datatraining')),

    path('knn/', include(('knn.urls', 'knn'), namespace='knn')),

    path('dtc/', include(('dtc.urls', 'dtc'), namespace='dtc')),

]
