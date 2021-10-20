"""
Django settings for visreport project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.gis',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'observations.apps.ObservationsConfig',
    'accounts.apps.AccountsConfig',
    'leaflet',
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

ROOT_URLCONF = 'visreport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["visreport","visreport/templates","visreport/accounts","visreport/accounts/templates/accounts", "observations/templates"],
        'APP_DIRS': False,
        'OPTIONS': {

            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],

            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'visreport.wsgi.application'

SERIALIZATION_MODULES = {
     "geojson": "django.contrib.gis.serializers.geojson",
  }


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Perth'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'visreport/static/')
]
STATIC_URL = '/static/'

STATIC_ROOT= os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

LEAFLET_CONFIG = {
  'TILES': 'https://api.mapbox.com/styles/v1/patrickmorrison1498/ck603l62s0mbi1io55kc8hif5/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoicGF0cmlja21vcnJpc29uMTQ5OCIsImEiOiJjazNoNDQ4dG4wMmppM21ya3BtbWc5am9iIn0.nLex7QBehGELoOf7j9OqHg',
  'SPATIAL_EXTENT': (124,-35.5 ,113.3,-30),
  'DEFAULT_CENTER': (-32.00,115.64),
  'DEFAULT_ZOOM': 10,
  'MIN_ZOOM': 7,
  'MAX_ZOOM': 12,
  'RESET_VIEW': False,
  'tap': True,
}

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCH_SECRET_KEY")

DEBUG = os.getenv("DEBUG", "False") == "True"
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

EMAIL_HOST=os.getenv("EMAIL_HOST")
EMAIL_HOST_USER=os.getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD=os.getenv("EMAIL_PASSWORD")
EMAIL_USE_TLS=True
EMAIL_PORT=os.getenv("EMAIL_PORT")

try:
    from .local_settings import *
except ImportError:
    pass