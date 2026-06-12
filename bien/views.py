from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bien.models import Bien, Categorie, Quartier
from bien.serializers import (
    BienSerializer,
    CategorieSerializer,
    QuartierSerializer)

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import DemandeVisite
from .serializers import DemandeVisiteSerializer

class BienViewSet(ModelViewSet):
    serializer_class = BienSerializer

    queryset = Bien.objects.all()

class CategorieViewSet(ModelViewSet):
    serializer_class = CategorieSerializer

    
    queryset = Categorie.objects.all()

class QuartierViewSet(ModelViewSet):
    serializer_class = QuartierSerializer

    
    queryset = Quartier.objects.all()

class DemandeVisiteCreateView(CreateAPIView):
    queryset = DemandeVisite.objects.all()
    serializer_class = DemandeVisiteSerializer
    permission_classes = [AllowAny]