# config/settings/staging.py
"""Settings for staging"""

# pylint: disable=locally-disabled, W0401, W0614
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Example using Postgres
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
