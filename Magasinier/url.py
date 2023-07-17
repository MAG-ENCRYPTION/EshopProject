from django.contrib.auth import admin
from django.urls import path
from Caissière.views import *
from AppMain.views import *

urlpatterns = [

    path('facturer/', Facturer, name='facturer'),
    #path('caisse/', dashbordcaissiere, name='dashbordcaisse'),
    path('', start, name='start'),
    path('log/', my_login, name='authenticate'),
    #path('log/<str:nomgest>', my_login, name='authenticate'),
    path('admin/', admin.admin.site.urls, name='admin'),
]