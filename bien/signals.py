from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import DemandeVisite

@receiver(post_save, sender=DemandeVisite)
def notifier_proprietaire(sender, instance, created, **kwargs):
    if created:
        bien = instance.bien
        proprietaire = bien.proprietaire
        
        # Sujet et contenu du mail
        sujet = f"Nouvelle demande de visite pour votre bien : {bien.titre}"
        message = f"""
        Bonjour {proprietaire.username},

        Vous avez reçu une nouvelle demande de visite pour votre bien "{bien.titre}".

        Détails du visiteur :
        - Nom : {instance.nom_visiteur}
        - Email : {instance.email_visiteur}
        - Téléphone : {instance.telephone_visiteur}
        - Date souhaitée : {instance.date_visite_souhaitee.strftime('%d/%m/%Y %H:%M')}

        Message du visiteur :
        "{instance.message}"

        Cordialement,
        L'équipe Immo.
        """
        
        # Envoi de l'email
        send_mail(
            subject=sujet,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[proprietaire.email],
            fail_silently=False, # Mettre à True en prod pour éviter de bloquer l'API si le serveur mail crash
        )