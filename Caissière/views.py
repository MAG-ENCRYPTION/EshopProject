from datetime import datetime
from django.shortcuts import *
from django.core.paginator import Paginator
from django.db import connection
from AppMain.models import *
from Magasinier.forms import *

BASE_LINK = 'http://boutiquebambino.shop/eshop/productImages/'
Slash = '/'
GEST = []
categories_list = Categorie.objects.all()
categorie_obj =  Categorie.objects


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            name = str(Gestionnaire.objects.get(login=username).login.__str__())
            password1 = str(Gestionnaire.objects.get(login=username).pwd.__str__())
            gest = str(Gestionnaire.objects.get(login=username).nomgest.__str__())
            type = int(Gestionnaire.objects.get(login=username).typegest.__str__())
            """link = 'http://boutiquebambino.shop/eshop/productImages/' + codeproduit
            r = list(Photo.objects.get(codepro=codeproduit).lienphoto)
            print(r)"""
            if name == str(username) and password1 == str(password):
                if type == 0:
                    return render(request, 'facturation.html', context={"gest": gest})
                if type == 1:
                    return render(request, 'DashbordMagasinier.html', context={"gest": gest})
            else:
                gest = "ras"
        except Gestionnaire.DoesNotExist:
            return None
    return render(request, 'authUser.html')


def authentification(request, username, password):
    try:
        user = Gestionnaire.objects.get(login=username, pwd=password)
        return user
    except Gestionnaire.DoesNotExist:
        return None


def AllCategorieCaisse(request):
    paginator = Paginator(categories_list, 10)  # 10 éléments par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'AllcategoriesCaisse.html', context)


def AllCategorieMag(request):
    paginator = Paginator(categories_list, 10)  # 10 éléments par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'AllcategoriesMag.html',context)


def ProduitCaisse(request):
    query = request.GET.get('query', '')
    order_by = request.GET.get('order_by', '')

    if query:
        produits_list = Produit.objects.filter(codepro__icontains=query)
    else:
        produits_list = Produit.objects.all()

    if order_by == 'qte':
        produits_list = produits_list.order_by('qte')

    paginator = Paginator(produits_list, 10)  # Afficher 10 produits par page
    page = request.GET.get('page')
    produits = paginator.get_page(page)

    context = {
        'produits': produits,
        'photos': Photo.objects.all()[:100],
    }
    return render(request, 'ProduitsCaisse.html', context)


def ProduitsMagasin(request):
    return render(request, 'magasinier/ProduitsMag.html')


def Facturer(request):
    return render(request, 'facturation.html')


def CategorieCaisse(request):
    return render(request, 'categorieCaisse.html')


def produits_par_categorie_caisse(request, nomcat):
    categorie = Categorie.objects.get(nomcat=nomcat)
    produits_list = Produit.objects.filter(idcategorie=categorie)
    paginator = Paginator(produits_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    produits = []
    for produit in page_obj:
        produit_dict = {
            'nompro': produit.nompro,
            'codepro': produit.codepro,
            'prix': produit.prix,
            'qte': produit.qte,
            'details': {
                'description': produit.description,
                'photo': None,
            },
        }
        photo = Photo.objects.filter(codepro=produit.codepro).first()
        if photo:
            produit_dict['photo'] = photo
            produit_dict['details']['photo'] = photo.lienphoto
        produits.append(produit_dict)
    context = {
        'categorie': categorie,
        'produits': produits,
        'page_obj': page_obj,
    }
    return render(request, 'ProduitsCaisse.html', context)


def produits_par_categorie_magasinier(request, nomcat):
    categorie = Categorie.objects.get(nomcat=nomcat)
    produits_list = Produit.objects.filter(idcategorie=categorie)
    paginator = Paginator(produits_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    produits = []
    for produit in page_obj:
        produit_dict = {
            'nompro': produit.nompro,
            'codepro': produit.codepro,
            'prix': produit.prix,
            'qte': produit.qte,
            'details': {
                'description': produit.description,
                'photo': None,
            },
        }
        photo = Photo.objects.filter(codepro=produit.codepro).first()
        if photo:
            produit_dict['photo'] = photo
            produit_dict['details']['photo'] = photo.lienphoto
        produits.append(produit_dict)
    context = {
        'categorie': categorie,
        'produits': produits,
        'page_obj': page_obj,
    }
    return render(request, 'ProduitsMag.html', context)


def MAG(request):
    return render(request, 'DashbordMagasinier.html')


def stock(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT DISTINCT YEAR(datestock) FROM gestionstock;')
        years = [row[0] for row in cursor.fetchall()]

    with connection.cursor() as cursor:
        cursor.execute('SELECT DISTINCT MONTH(datestock) FROM gestionstock;')
        months = [row[0] for row in cursor.fetchall()]

    produits = []

    All_stocks = Gestionstock.objects.all()
    if request.method == 'GET':
        code = request.GET.get('code', None)
        mois = request.GET.get('mois', None)
        annee = request.GET.get('annee', None)
        if code:
            All_stocks = All_stocks.filter(codepro=code)
        if annee and mois:
            date_min = datetime(int(annee), int(mois), 1)
            date_max = datetime(int(annee), int(mois) + 1, 1)
            All_stocks = All_stocks.filter(datestock__gte=date_min, datestock__lt=date_max)
        if annee:
            date_min = datetime(int(annee), 1, 1)
            date_max = datetime(int(annee) + 1, 1, 1)
            All_stocks = All_stocks.filter(datestock__gte=date_min, datestock__lt=date_max)

    paginator = Paginator(All_stocks, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for gs in page_obj:
        produit = Produit.objects.get(codepro=gs.codepro.codepro)
        gestionnaire = Gestionnaire.objects.get(idgest=gs.idgest.idgest)
        categorie = produit.idcategorie.nomcat
        if gs.operation == 1:
            operation = "Ajout"
        else:
            operation = "Retrait"
        produits.append({
            'nom_produit': produit.nompro,
            'code_produit': produit.codepro,
            'nom_gestionnaire': gestionnaire.nomgest,
            'quantite': gs.qte,
            'categorie_produit': categorie,
            'action': operation,
            'date_stock': gs.datestock,
        })

    return render(request, 'magasinier/stocks.html',
                  {'years': years, 'page_obj': page_obj, 'months': months, 'produits': produits})


def testr(request):
    r = 1
    return render(request, 'test.html', context={"link": r})


def test(request):
    query = request.GET.get('query', '')
    order_by = request.GET.get('order_by', '')

    if query:
        produits_list = Produit.objects.filter(codepro__icontains=query)
    else:
        produits_list = Produit.objects.all()

    if order_by == 'qte':
        produits_list = produits_list.order_by('qte')

    paginator = Paginator(produits_list, 10)  # Afficher 10 produits par page
    page = request.GET.get('page')
    produits = paginator.get_page(page)

    context = {
        'produits': produits,
    }
    return render(request, 'test.html', context)


def prod(request):
    produits = []
    All_stocks = Produit.objects.all()[:20]
    if request.method == 'GET':
        code = request.GET.get('code', None)
        codefour = request.GET.get('codefour', None)
        quanti = request.GET.get('quanti', None)
        if code:
            All_stocks = All_stocks.filter(codepro=code)
        if quanti:
            All_stocks = All_stocks.all().filter(qte=quanti)
        if codefour:
            All_stocks = All_stocks.filter(codearrivage=codefour)

    paginator = Paginator(All_stocks, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for gs in page_obj:
        photos = []
        photos = Photo.objects.all().filter(codepro=gs)
        categorie = Categorie.objects.get(idcat=gs.idcategorie.idcat)
        produits.append({
            'nom': gs.nompro,
            'code': gs.codepro,
            'codepro': gs.codepro,
            'prix': gs.prix,
            'photo': photos[0],
            'quantite': gs.qte,
            'categorie': categorie.nomcat,
            'codefour': gs.codearrivage,
            'size1': gs.size1,
            'size2': gs.size2,
            'description': gs.description,
            'photos': photos,
        })
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('magasinier/Produits.html')
    else:
        form = ProduitForm()

    return render(request, 'magasinier/ProduitsMagasinier.html', {'page_obj': page_obj, 'produits': produits, 'form': form})