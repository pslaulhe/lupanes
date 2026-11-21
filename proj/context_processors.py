from django.conf import settings

from lupanes import get_version
from lupanes.feature_flags import WIZARD_EXAMPLE_FRONTEND_FLAG


def metadata(request):
    return {
        "version": get_version(),
        "posthog_project_token": settings.POSTHOG_PROJECT_TOKEN,
        "posthog_host": settings.POSTHOG_HOST,
        "posthog_frontend_flag_key": WIZARD_EXAMPLE_FRONTEND_FLAG,
        "debug": settings.DEBUG,
    }
