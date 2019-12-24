from decouple import Csv

from .base import *

DEBUG = config('DEBUG', default=False)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': '5432',
        'NAME': config('DB_NAME', default=''),
        'USER': config('DB_USER_NAME', default=''),
        'PASSWORD': config('DB_PASS', default=''),
    }
}