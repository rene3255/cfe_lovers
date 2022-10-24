from .base import *
DEBUG = os.environ.get("DEBUG", default=False)
ALLOWED_HOSTS = [".herokuapp.com"]

DATABASES = {
        'default': dj_database_url.config()
            
    }

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True


