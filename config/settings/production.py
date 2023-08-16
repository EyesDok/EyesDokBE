from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['noonddock.site'] 

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DJANGO_APPS +=[

]
PROJECT_APPS +=[

]
THIRD_PARTY_APPS +=[

]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#static 디렉터리 지정
STATIC_ROOT = BASE_DIR / 'static'
