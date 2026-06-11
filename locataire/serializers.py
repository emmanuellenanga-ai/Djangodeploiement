from rest_framework.serializers import ModelSerializer
from locataire.models import Locataire

class LocataireSerializer(ModelSerializer):
     class Meta:
        model= Locataire
        fields = '__all__'
