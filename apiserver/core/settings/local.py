from .base import *  # noqa
from .base import INSTALLED_APPS

DEBUG = True

INSTALLED_APPS += [
    'rest_framework',
    'drf_spectacular',
    'system',
    'myapp',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_VERSIONING_CLASS': 'common.drf.versioning.APIVersioning',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DRF APIServer',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    # 'SERVE_INCLUDE_SCHEMA': False,
}
