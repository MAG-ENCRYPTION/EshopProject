from django.contrib.auth import admin
from django.urls import path
from Caissière.views import *
from AppMain.views import *

urlpatterns = [
    path('prodCaisse/', ProduitCaisse, name='produitsCaisse'),
    path('magaprod/',prod,name='produit'),
    path('prodMagasinier/', ProduitsMagasin, name='prodMag'),
    path('caisse/', Facturer, name='facturer'),
    path('stocks/', stock, name='stock'),
    path('mag/', MAG, name='dashbordmagasinier'),
    path('AllCategorieC/', AllCategorieCaisse, name='AllCategoCaisse'),
    path('AllCategorieM/', AllCategorieMag, name='AllCategoMAG'),
    path('CategorieCaissess/<str:nomcat>', produits_par_categorie_caisse, name='categorie_spe'),
    path('CategorieMagasinier/<str:nomcat>', produits_par_categorie_magasinier, name='categorie_spe_mag'),
    path('', start, name='start'),
    path('test/', test, name='test'),
    path('login/', my_login, name='authenticate'),
    path('admin/', admin.admin.site.urls, name='admin'),
]
