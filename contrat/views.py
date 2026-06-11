from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from contrat.models import Contrat
from contrat.serializers import ContratSerializer


class ContratViewSet(ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
# Create your views here.
