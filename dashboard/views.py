from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bien.models import Bien 
from locataire.models import Locataire
from contrat.models import Contrat
from paiement.models import Paiement


@api_view(['GET'])
def dashboard_stats(request):

    total_loyers = sum(
        paiement.montant_paye
        for paiement in Paiement.objects.all()
    )
    data = {
        'total_biens' : Bien.objects.count(),
        'biens_disponibles': Bien.objects.filter(statut='Disponible').count(),
        'biens_occupes': Bien.objects.filter(statut='Occupé').count(),
        'total_locataire': Locataire.objects.count(),
        'contrats_actifs': Contrat.objects.filter(statut='Actif').count(),
        'loyers_encaisses': total_loyers



    }

    return Response(data)
