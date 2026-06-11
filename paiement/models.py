from django.db import models
from contrat.models import Contrat 


class Paiement(models.Model):
    MODE_CHOICES = [
        ('Espèces','Espèces'),
        ('Mobile Money','Mobile Money'),
        ('Orange Money','Orange Money' ),
        ('Virement','Virement'),
        ('Cheque','Cheque'),
    ]

    reference = models.CharField(max_length=50)
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE, related_name='paiement')
    montant_du = models.DecimalField(max_digits=12, decimal_places=0)
    montant_paye = models.DecimalField(max_digits=12, decimal_places=0)
    montant_restant = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_paiement = models.DateTimeField()
    mois_concerne = models.CharField(max_length=50)
    mode = models.CharField(
        max_length=50,
        choices=MODE_CHOICES,
        default='Espèces'
    )
    note = models.TextField(blank=True)

    def _str_(self):
        return self.reference