from django.db import models
from proprietaire.models import Proprietaire
from django.contrib.auth.models import AbstractUser


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

class DemandeVisite(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='demandes_visite')
    nom_visiteur = models.CharField(max_length=100)
    email_visiteur = models.EmailField()
    telephone_visiteur = models.CharField(max_length=20)
    date_visite_souhaitee = models.DateTimeField()
    message = models.TextField(blank=True)
    cree_le = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Demande pour {self.bien.titre} par {self.nom_visiteur}"

