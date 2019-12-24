from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': config('DB_NAME', default=''),
        'USER': config('DB_USER_NAME', default=''),
        'PASSWORD': config('DB_PASS', default=''),
    }
}