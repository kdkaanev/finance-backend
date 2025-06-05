from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.user'

    def ready(self):
        # Import signals to ensure they are registered
        import backend.user.signals
