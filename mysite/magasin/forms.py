from pyexpat import model
from django.forms import ModelForm
from .models import Commande, Fournisseur, Produit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProduitForm(forms.ModelForm):
    class Meta :
        model = Produit
        fields ="__all__" #pour tous les champs de la table
        
        widgets = {
            'libelle' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'prix' : forms.TextInput(attrs={'class': 'form-control'}),
            'type' : forms.Select(attrs={'class': 'form-control'}),
            'img' : forms.FileInput(attrs={'required': False,'class': 'form-control','enctype': 'multipart/form-data'}),
            'ctgr' : forms.Select(attrs={'class': 'form-control'}),
            'fournisseur' : forms.Select(attrs={'class': 'form-control'}),
        }
        
#fields=['libelle','description'] #pour qulques champs
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"
        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.Textarea(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
        widgets = {
            'DateCde' : forms.DateTimeInput(attrs={'class': 'form-control'},format="%d - %m - %Y"),
            'totalCde' : forms.TextInput(attrs={'class': 'form-control'}),
            'produits' : forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail') 
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }