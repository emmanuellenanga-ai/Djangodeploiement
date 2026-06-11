from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from paiement.models import Paiement
from paiement.serializers import PaiementSerializer


class PaiementViewSet(ModelViewSet):
    serializer_class = PaiementSerializer

    def get_queryset(self):
        return Paiement.objects.all()
# Create your views here.
