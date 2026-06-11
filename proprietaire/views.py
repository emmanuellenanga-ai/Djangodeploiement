from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from proprietaire.models import Proprietaire
from proprietaire.serializers import ProprietaireSerializer


class ProprietaireViewSet(ModelViewSet):
    serializer_class = ProprietaireSerializer

    def get_queryset(self):
        return Proprietaire.objects.all()
# Create your views here.
