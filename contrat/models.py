from django.db import models
from locataire.models import Locataire
from bien.models import Bien


class Contrat(models.Model):
    STATUT_CHOICES = [
        ('Actif', 'Actif'),
        ('Expiré', 'Expiré'),
        ('Résilié', 'Résilié'),
    ]
    
    reference = models.CharField(max_length=60, unique=True)
    bien = models.ForeignKey(Bien, on_delete=models.PROTECT)
    locataire = models.ForeignKey(Locataire, on_delete=models.PROTECT)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant = models.DecimalField(max_digits=12, decimal_places=0)
    caution = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    statut = models.CharField(
        max_length=50,
        choices= STATUT_CHOICES,
        default='Actif'

    )
    date_creation = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def _str_(self):
        return self.reference

