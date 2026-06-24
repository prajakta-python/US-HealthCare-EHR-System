"""
Django settings for US Healthcare EHR backend.

Secrets ('.env' file madhun) read karnyasathi python-decouple vaaprat aahot.
KADHIHI SECRET_KEY / password ithe hardcode karaycha nahi.
"""

from pathlib import Path
from decouple import config, Csv

# Project cha base folder (jithe manage.py aahe)
BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY — sagle secrets .env madhun yetat
# ============================================================
SECRET_KEY = config('SECRET_KEY')                       # .env madhun
DEBUG = config('DEBUG', default=False, cast=bool)       # dev la True, prod la False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())  # comma-separated list


# ============================================================
# APPLICATIONS
# ============================================================
# Django che built-in apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Bahercha (third-party) packages je apan install kele
THIRD_PARTY_APPS = [
    'rest_framework',           # DRF — API banavnyasathi
    'drf_spectacular',          # Swagger / OpenAPI docs
    'django_filters',           # Search / filter APIs
    'corsheaders',              # Frontend (vegla domain) connect karaycha asel tar
]

# Apan svatah banavnar te apps (atta rikame — Phase 2 pasun bharu)
LOCAL_APPS = [
    # 'apps.users',
    # 'apps.patients',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',             # CORS — saglyat var pahije
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# ============================================================
# DATABASE — PostgreSQL (Docker), settings .env madhun
# ============================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'          # Healthcare madhe time UTC madhe thevtat (jagbharat consistent)
USE_I18N = True
USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# DJANGO REST FRAMEWORK (DRF) — API cha vartan
# ============================================================
REST_FRAMEWORK = {
    # Login kasa check karaycha (Phase 2 la JWT add karu)
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    # Default la: login aslyashivay kahi disnar nahi
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # Swagger docs sathi schema generator
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # Pagination — ekach veli sagla data nako, page-page ne
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    # Filter / search / ordering
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}


# ============================================================
# SWAGGER / OpenAPI (drf-spectacular)
# ============================================================
SPECTACULAR_SETTINGS = {
    'TITLE': 'US Healthcare EHR API',
    'DESCRIPTION': 'Production-style US Healthcare EHR backend — Django REST Framework',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


# ============================================================
# CORS — kontya frontend la API vapraychi parvangi
# ============================================================
CORS_ALLOW_ALL_ORIGINS = True   # development sathi. Production la specific domains thevu.
