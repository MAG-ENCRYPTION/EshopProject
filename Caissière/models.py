from django.db import models
from AppMain.models import *


class Categorie(models.Model):
    idcat = models.AutoField(db_column='idCat', primary_key=True)  # Field name made lowercase.
    nomcat = models.CharField(db_column='nomCat', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'
