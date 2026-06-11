from django.db import models


class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    adresse = models.TextField(blank=True)

def _str_(self):
    return f"{self.nom} {self.prenom}"
