from django.apps import AppConfig


class LupanesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lupanes'

    def ready(self):
        from lupanes.posthog_logs import configure_posthog_log_export

        configure_posthog_log_export()
