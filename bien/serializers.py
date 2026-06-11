from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from bien.models import Bien, Categorie , Quartier

class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

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
