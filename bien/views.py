from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bien.models import Bien, Categorie, Quartier
from bien.serializers import (
    BienSerializer,
    CategorieSerializer,
    QuartierSerializer)


class BienViewSet(ModelViewSet):
    serializer_class = BienSerializer

    queryset = Bien.objects.all()

class CategorieViewSet(ModelViewSet):
    serializer_class = CategorieSerializer

    
    queryset = Categorie.objects.all()

class QuartierViewSet(ModelViewSet):
    serializer_class = QuartierSerializer

    
    queryset = Quartier.objects.all()

