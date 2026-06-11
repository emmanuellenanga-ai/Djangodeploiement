from django.db import models
from proprietaire.models import Proprietaire


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def _str_(self):
        return self.nom

class Quartier(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=20, default='Yaoundé')

    def _str_(self):
        return f"{self.nom} - {self.ville}"

class Bien(models.Model):
    STATUT_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Occupé', 'Occupé'),
        ('En rénovation', 'En rénovation'),
    ]
    titre = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    quartier = models.ForeignKey(Quartier, on_delete=models.PROTECT)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    prix_mensuel = models.DecimalField(max_digits=12, decimal_places=0)
    caution = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    surface = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nombre_chambre = models.PositiveIntegerField (default=1)
    nombre_salle_de_bain =  models.PositiveIntegerField (default=1)
    photo = models.ImageField(upload_to='bien/', blank=True, null=True)
    statut = models.CharField(
        max_length=30,
        choices=STATUT_CHOICES,
        default='Disponible'

    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titre

