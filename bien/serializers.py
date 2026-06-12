from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from bien.models import Bien, Categorie , Quartier
from .models import DemandeVisite


class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class DemandeVisiteSerializer(ModelSerializer):
    class Meta:
        model = DemandeVisite
        fields = ['id', 'bien', 'nom_visiteur', 'email_visiteur', 'telephone_visiteur', 'date_visite_souhaitee', 'message', 'cree_le']
        read_only_fields = ['id', 'cree_le']

class QuartierSerializer(ModelSerializer):
    class Meta:
        model = Quartier
        fields = '__all__'

class BienSerializer(ModelSerializer):
    categorie_nom = serializers.CharField(
        source='categorie.nom',
        read_only=True
    )
    quartier_nom = serializers.CharField(
        source='quartier.nom',
        read_only=True
    )
    proprietaire_nom = serializers.CharField(
        source='proprietaire.nom',
        read_only=True
    )


    class Meta:
        model= Bien
        fields = '__all__'
