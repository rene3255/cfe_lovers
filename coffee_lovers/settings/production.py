from pathlib import Path
import dj_database_url
import environ
import os
from decouple import config
from .base import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
environ.Env.read_env()

#env.read_env(os.path.join(BASE_DIR, 'coffee_lovers/.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUGG')

ALLOWED_HOSTS = list(config('ALLOWED_HOSTSS')) 



ROOT_URLCONF = 'coffee_lovers.urls'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(
      default=config('DATABASE_URL')
    )
      
}




cloudinary.config( 
  cloud_name = "dlx8oaq0o", 
  api_key = "169133284948194", 
  api_secret = "aiKg95q_d1bZ7Dg6wbAEXH0PUZ4" 
)
