from django.db import models


class Categorie(models.Model):
    idcat = models.AutoField(db_column='idCat', primary_key=True)  # Field name made lowercase.
    nomcat = models.CharField(db_column='nomCat', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'


class Facture(models.Model):
    idfac = models.AutoField(db_column='idFac', primary_key=True)  # Field name made lowercase.
    datefac = models.DateTimeField(db_column='dateFac')  # Field name made lowercase.
    remise = models.DecimalField(max_digits=4, decimal_places=2)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    tel = models.CharField(max_length=15, blank=True, null=True)
    typefac = models.PositiveSmallIntegerField(db_column='typeFac', db_comment='0 = cash, 1 = eMoney, 2 = tontine, 3 = point, 4 = autres')  # Field name made lowercase.
    idcaissiere = models.ForeignKey('Gestionnaire', models.DO_NOTHING, db_column='idCaissiere')  # Field name made lowercase.
    capital = models.DecimalField(max_digits=10, decimal_places=2, db_comment='capital = sommes des prixAchat des produits vendus')
    tva = models.DecimalField(max_digits=10, decimal_places=2, db_comment="tva s'applique sur la valeur ajoutÚ")
    codepromo = models.CharField(db_column='codePromo', max_length=15, blank=True, null=True, db_comment="codePromo va permettre d'identifizezr un influenceur ou simplement justifier une reduction speciale")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facture'


class Gestionnaire(models.Model):
    idgest = models.AutoField(db_column='idGest', primary_key=True)  # Field name made lowercase.
    nomgest = models.CharField(db_column='nomGest', max_length=45)  # Field name made lowercase.
    typegest = models.IntegerField(db_column='typeGest', db_comment='0 = caissiere, 1 = Magasinier,   2 = webGest, 3 = tontine et autres, 4 = superadmin')  # Field name made lowercase.
    login = models.CharField(unique=True, max_length=20)
    pwd = models.CharField(max_length=20)
    actif = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gestionnaire'
        unique_together = (('login', 'pwd', 'actif'),)


class Gestionstock(models.Model):
    idstock = models.AutoField(db_column='idStock', primary_key=True)  # Field name made lowercase.
    qte = models.PositiveIntegerField()
    datestock = models.DateTimeField(db_column='dateStock')  # Field name made lowercase.
    operation = models.IntegerField()
    idgest = models.ForeignKey(Gestionnaire, models.DO_NOTHING, db_column='idGest')  # Field name made lowercase.
    codepro = models.ForeignKey('Produit', models.DO_NOTHING, db_column='codePro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gestionstock'



class Photo(models.Model):
    idphoto = models.AutoField(db_column='idPhoto', primary_key=True)  # Field name made lowercase.
    lienphoto = models.CharField(db_column='lienPhoto', max_length=150)  # Field name made lowercase.
    codepro = models.ForeignKey('Produit', models.DO_NOTHING, db_column='codePro')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'photo'


class Produit(models.Model):
    codepro = models.PositiveIntegerField(db_column='codePro', primary_key=True)  # Field name made lowercase.
    nompro = models.CharField(db_column='nomPro', max_length=100)  # Field name made lowercase.
    prix = models.DecimalField(max_digits=8, decimal_places=0)
    qte = models.PositiveIntegerField()
    description = models.CharField(max_length=240)
    codearrivage = models.CharField(db_column='codeArrivage', max_length=250)  # Field name made lowercase.
    actif = models.IntegerField()
    idcategorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='idCategorie')  # Field name made lowercase.
    dateinsertion = models.DateTimeField(db_column='dateInsertion', blank=True, null=True)  # Field name made lowercase.
    prixachat = models.DecimalField(db_column='prixAchat', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pourcentage = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    promo = models.IntegerField(blank=True, null=True, db_comment="promo prendra la valeur 0 lorsqu'on souhaite faire une promotion")
    size1 = models.IntegerField(blank=True, null=True, db_comment='la plus petite taille de la serie')
    size2 = models.IntegerField(blank=True, null=True, db_comment='la plus grande taille de la serie')
    typesize = models.IntegerField(db_column='typeSize', blank=True, null=True, db_comment='typeSize = 0 pour Mois, 1 pour Annee, 2 indique plutot la taille des chaussures, 3 taille Vetement Adulte')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produit'
