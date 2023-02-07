import os
from environs import Env
import dj_database_url

env = Env()
env.read_env()
DATABASES = {'default': dj_database_url.config(default=env.str('DB_URL'))}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY', default='MY_KEY')

DEBUG = env.bool("DEBUG", default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
