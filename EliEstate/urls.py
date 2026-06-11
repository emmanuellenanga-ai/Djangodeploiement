"""
URL configuration for EliEstate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from proprietaire.views import ProprietaireViewSet
from bien.views import (
    BienViewSet,
    CategorieViewSet,
    QuartierViewSet
    )
from locataire.views import LocataireViewSet
from contrat.views import ContratViewSet
from paiement.views import PaiementViewSet
 
router_proprietaire = routers.SimpleRouter()
router_proprietaire.register('proprietaire', ProprietaireViewSet, basename='proprietaire')

router_locataire = routers.SimpleRouter()
router_locataire.register('locataire', LocataireViewSet, basename='locataire')

router_bien = routers.SimpleRouter()
router_bien.register('bien', BienViewSet, basename='bien')
router_bien.register('categorie', CategorieViewSet, basename='categorie')
router_bien.register('quartier', QuartierViewSet, basename='quartier')


router_contrat = routers.SimpleRouter()
router_contrat.register('contrat', ContratViewSet, basename='contrat')

router_paiement = routers.SimpleRouter()
router_paiement.register('paiement', PaiementViewSet, basename='paiement')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/',include(router_proprietaire.urls)),
    path('api/',include(router_locataire.urls)),
    path('api/',include(router_bien.urls)),
    path('api/',include(router_contrat.urls)),
    path('api/',include(router_paiement.urls)),
    path('api/dashboard',include('dashboard.urls')),
    

]
