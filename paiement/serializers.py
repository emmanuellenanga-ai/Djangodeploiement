from rest_framework.serializers import ModelSerializer
from paiement.models import Paiement

class PaiementSerializer(ModelSerializer):
     class Meta:
        model= Paiement
        fields = '__all__'