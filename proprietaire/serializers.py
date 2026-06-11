from rest_framework.serializers import ModelSerializer
from proprietaire.models import Proprietaire

class ProprietaireSerializer(ModelSerializer):
     class Meta:
        model= Proprietaire
        fields = '__all__'
