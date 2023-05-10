from django.urls import URLPattern, path,include
from . import views
#from rest_framework import routers
#from magasin.views import ProduitViewSet

#router = routers.DefaultRouter()
#router.register(r'magasin', ProduitViewSet)

urlpatterns=[
    #path('', include(router.urls)),
    path("",views.index),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('majP/',views.majP),
    path('AjoutCom/',views.AjoutCom),
    path('home/',views.home,name="home"),
    path('prod/',views.mag,name="prod"),
    path('listProd/',views.ListProd),
    path('listFour/',views.ListFournisseurs),
    path('adminPanelAc/',views.adminPanelAc),
    path('ListCom/',views.ListCommande),
    path('register/',views.register, name = 'register'),
]