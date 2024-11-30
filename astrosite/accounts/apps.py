from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'astrosite.accounts'

    def ready(self):
        import astrosite.accounts.signals
