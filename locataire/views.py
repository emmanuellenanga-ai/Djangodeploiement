from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from locataire.serializers import LocataireSerializer
from locataire.models import Locataire

class LocataireViewSet(ModelViewSet):
    serializer_class = LocataireSerializer

    def get_queryset(self):
        return Locataire.objects.all()
