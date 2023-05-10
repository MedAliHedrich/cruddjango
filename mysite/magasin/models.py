from distutils.command.upload import upload
import email
from datetime import date
from email.policy import default
from logging import PlaceHolder
from tkinter import CASCADE, MULTIPLE
from django.db import models

class Categorie(models.Model):
    Type_Choices=[
        ('AI','Alimentaire'),
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Vs','Vaisselle'),
        ('Vt', 'Vetement'),
        ('Jx', 'Jouets'),
        ('Lg','Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor')
    ]
    name=models.CharField(max_length=50,choices=Type_Choices,default='Alimentaire')
    def __str__(self):
        return 'name : '+self.name;

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='Tunis')
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "nom : "+self.nom

class Produit(models.Model):
    Type_Choices=[
        ('em','emballe'),
        ('fr', 'frais'),
        ('cs', 'conserve')
    ]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='non definie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=Type_Choices,default='em')
    img=models.ImageField(blank=True,upload_to='media/')
    ctgr=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return "libelle : "+self.libelle+" Description : "+self.description+" Prix : "+str(self.prix)+ " type : "+self.type

class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)

    def __str__(self):
        return "libelle : "+self.libelle+" Prix : "+str(self.prix)+ "Garantie : "+self.Duree_garantie

class Commande(models.Model):
    DateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField(Produit)
    
    def __str__(self):
        return "Date : "+str(self.DateCde)+" quantite : "+str(self.totalCde)

# Create your models here.
