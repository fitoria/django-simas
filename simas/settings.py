# Django settings for simas project

from local_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
AUTH_PROFILE_MODULE = "pagina.UserProfile"
DEFAULT_CHARSET = 'utf-8'
MANAGERS = ADMINS
DATABASE_ENGINE = 'mysql'
SEARCH_ENGINE = 'mysql'
ACCOUNT_ACTIVATION_DAYS = 7
SITE_ID = 1
USE_I18N = True
ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


MEDIA_ROOT = os.path.join(SITE_ROOT,'media')
MEDIA_URL = '/media'
TEMPLATE_DIRS = (
SITE_ROOT+"/templates",
)
ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'profiles',
    'django_evolution',
    'pagina',
) 

