# config/settings/development.py
"""Settings for development"""

from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


INTERNAL_IPS = ['127.0.0.1', 'localhost', ]

# comment if using postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.getenv('DATABASE_NAME_DEV'),
#         'USER': os.getenv('DATABASE_USER_DEV'),
#         'PASSWORD': os.getenv('DATABASE_PASSWORD_DEV'),
#         'HOST': '',
#         'PORT': '',
#     }
# }
