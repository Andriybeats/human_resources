import dj_database_url
import django_heroku

from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL',
                                                     default=''),
                                      conn_max_age=4000)
}

django_heroku.settings(locals())
