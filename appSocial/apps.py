from django.apps import AppConfig


class AppsocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appSocial'

    def ready(self):
        import appSocial.signals