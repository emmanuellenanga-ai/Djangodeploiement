from django.apps import AppConfig


class BienConfig(AppConfig):
    name = 'bien'

def ready(self):
    import bien.signals
