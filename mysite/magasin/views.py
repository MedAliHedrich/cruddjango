from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import CommandeForm, ProduitForm,UserCreationForm
from .forms import FournisseurForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import CreateView
#from rest_framework import viewsets
#from .serializers import ProduitSerializers



def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('/magasin/prod/')
    else :
         form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})


def home(request):
    list=Produit.objects.all()
    return render( request,'magasin/vitrine.html',{'list':list})

def index(request):   
    return render( request,'acceuil.html')

@login_required
def adminPanelAc(request):   
    return render( request,'magasin/adminPanelAc.html')    

@login_required
def ListProd(request):   
    list=Produit.objects.all()
    return render( request,'magasin/listProd.html',{'list':list})

@login_required
def ListFournisseurs(request):   
    list=Fournisseur.objects.all()
    return render( request,'magasin/listFournisseur.html',{'list':list})

@login_required
def ListCommande(request):   
    list=Commande.objects.all()
    return render( request,'magasin/ListCommande.html',{'list':list})

def mag(request):   
    list=Produit.objects.all()
    return render( request,'magasin/vitrine.html',{'list':list})

def nouveauFournisseur(request):
    if request.method=="POST":
        form=FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/listFour')
    else:
        form=FournisseurForm()
    return render(request,'magasin/fournisseur.html',{'form':form})
def majP(request):
    if request.method=="POST":
        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/prod')
    else:
        form=ProduitForm
    return render(request,'magasin/majProduits.html',{'form':form})


def AjoutCom(request):
    if request.method=="POST":
        form=CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/ListCom')
    else:
        form=CommandeForm
    return render(request,'magasin/AjoutCom.html',{'form':form})



#class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializers

# Create your views here.
