from .base import *
DEBUG = ENV.bool("DEBUG", default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.environ.get('DB_NAME',3)),
        'USER': str(os.environ.get('DB_USER')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD')),
        'HOST': str(os.environ.get('DB_HOST')),
        'PORT': os.environ.get('DB_PORT'),
    }
}