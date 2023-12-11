from .base import *

ALLOWED_HOSTS = ["52.79.107.37"]
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'Uwrvuzs)uP>oC56&dV8gfa>#aj;Dea~`',
        'HOST': 'ls-22c264be22bc827757f101650c780eaa16114811.c3kvi9sgwvge.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
