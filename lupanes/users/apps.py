from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from posthog import identify_context


@receiver(user_logged_in)
def identify_posthog_user(sender, request, user, **kwargs):
    """Identify the authenticated user in the current login request context."""
    identify_context(str(user.pk))
    if settings.POSTHOG_MW_CLIENT:
        settings.POSTHOG_MW_CLIENT.capture("user_logged_in")


class UsersConfig(AppConfig):
    name = 'lupanes.users'
