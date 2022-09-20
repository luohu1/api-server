from rest_framework.versioning import URLPathVersioning


class APIVersioning(URLPathVersioning):
    default_version = 'v1'
    allowed_versions = ['v1', 'v2', 'v3']
    version_param = 'version'
