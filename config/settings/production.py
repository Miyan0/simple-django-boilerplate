# config/settings/production.py
"""Settings for production"""

# pylint: disable=locally-disabled, W0401, W0614
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# example if using Postgres
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.getenv('DATABASE_NAME'),
#         'USER': os.getenv('DATABASE_USER'),
#         'PASSWORD': os.getenv('DATABASE_PASSWORD'),
#         'HOST': '',
#         'PORT': '',
#     }
# }
