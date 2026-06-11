from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrateur'),
        ('AGENT', 'Agent immobilier'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='AGENT'
    )
    telehone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(
        upload_to='utilisateurs/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
