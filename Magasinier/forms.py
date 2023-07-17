from django import forms
from AppMain.models import Produit


class ProduitForm(forms.ModelForm):
    

    class Meta:
        model = Produit
        fields = ['codepro','nompro','prix','qte','description','codearrivage','actif','idcategorie','dateinsertion','prixachat','pourcentage','promo','size1','size2','typesize']
        labels = {
            'codepro':' codepro',
            'nompro':' nompro',
            'prix':' prix',
            'qte':' qte',
            'description':' description',
            'codearrivage':' codearrivage',
            'actif':' actif',
            'idcategorie':' idcategorie',
            'dateinsertion':' dateinsertion',
            'prixachat':' prixachat',
            'pourcentage':' pourcentage',
            'promo':' promo',
            'size1':' size1',
            'size2':' size2',
            'typesize':' typesize'}


