"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import datetime
from email.utils import getaddresses
from pathlib import Path

import environ
from django.utils.crypto import get_random_string

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load conf from environment
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(Path(BASE_DIR, '.env'))

# sentry.io app monitoring platform (optional)
if env('SENTRY_DSN', default=None):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=env('SENTRY_DSN'),
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=0.2,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=list, default=[])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'django_extensions',
    'post_office',
    'lupanes',
    'lupanes.users',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Our context processor:
                "proj.context_processors.metadata",
            ],
        },
    },
]

WSGI_APPLICATION = 'proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = "users.User"


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True

# NOTE WARNING: on Django 3.2 USE_L10N is False by default but since 4.0 default is True
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = env('STATIC_ROOT')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# TODO(@slamora): disabled ManifestStatic because causes 500 error on /offline/ pwa page
# if not DEBUG:
#     STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = 'media/'

MEDIA_ROOT = env('MEDIA_ROOT')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')

EMAIL_BACKEND = env('EMAIL_BACKEND', default='post_office.EmailBackend')

EMAIL_HOST = env('EMAIL_HOST', default='localhost')

EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')

EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

EMAIL_PORT = env('EMAIL_PORT', default=25, cast=int)

EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[albaranes] ')

EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=False, cast=bool)

EMAIL_USE_SSL = env('EMAIL_USE_SSL', default=False, cast=bool)

EMAIL_TIMEOUT = 5

POST_OFFICE = {
    'MAX_RETRIES': 4,
    'RETRY_INTERVAL': datetime.timedelta(minutes=2),
}

ADMINS = getaddresses([env('ADMINS', default='[]',)])

MANAGERS = getaddresses([env('MANAGERS', default='[]',)])

# Authentication
LOGIN_URL = 'users:login'

LOGIN_REDIRECT_URL = 'lupanes:dashboard'

LOGOUT_REDIRECT_URL = LOGIN_URL

# Configure logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} [{levelname}] {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'lupanes': {
            'level': env('DJANGO_LOG_LEVEL', default='WARNING'),
            'handlers': ['console'],
        },
    },
}


# PWA (django-pwa)

PWA_APP_DEBUG_MODE = DEBUG

PWA_APP_NAME = 'Albaranes Lupierra'
PWA_APP_DESCRIPTION = "Albaranes digitales Lupierra"
PWA_APP_THEME_COLOR = '#ffffff'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        "src": "/static/android-chrome-192x192.png",
        "sizes": "192x192",
        "type": "image/png"
    },
    {
        "src": "/static/android-chrome-512x512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
PWA_APP_ICONS_APPLE = [{
    'src': '/static/apple-touch-icon.png',
    'sizes': '180x180'
}]
PWA_APP_SPLASH_SCREEN = [{
    'src': '/static/android-chrome-512x512.png',
    'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
}]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'es-ES'


# Lupierra custom settings
LUPIERRA_BASIC_AUTH_PASS = env("LUPIERRA_BASIC_AUTH_PASS", default=get_random_string(16))

LUPIERRA_GSPREAD_AUTH_PATH = env("LUPIERRA_GSPREAD_AUTH_PATH")

LUPIERRA_CUSTOMERS_BALANCE_URL = env("LUPIERRA_CUSTOMERS_BALANCE_URL")
