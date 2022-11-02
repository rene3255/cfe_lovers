

from pathlib import Path
import environ
import os
from .base import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

DEBUG = env.bool('DEBUGG', default=False)


ALLOWED_HOSTS = ["*"]  # tuple(env.list('ALLOWED_HOSTSS', default=["*"]))

# Application definition

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'coffee_lovers.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.environ.get('DB_NAME')),
        'USER': str(os.environ.get('DB_USER')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD')),
        'HOST':str(os.environ.get('DB_HOST')),
        'PORT':os.environ.get('DB_PORT'),
    }
}
   
   




# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/coffees_images/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'coffees_images')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),

)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
