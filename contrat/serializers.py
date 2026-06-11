from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from contrat.models import Contrat

class ContratSerializer(ModelSerializer):
    bien_nom = serializers.CharField(
        source='bien.titre',
        read_only=True
    )
    locataire_nom = serializers.CharField(
        source='locataire.nom',
        read_only=True
    )
    class Meta:
        model= Contrat
        fields = '__all__'