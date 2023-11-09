from .base import * #noqa
from .base import env


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="628PHlxAAp8Z0eKCG6-W_nWVTJBub_HEF8-2UzrsY8aI1L10ihI",
)

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "https://8080-vinneyj-customermanager-77d3wqof9um.ws-eu106.gitpod.io"]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["8080-vinneyj-customermanager-77d3wqof9um.ws-eu106.gitpod.io"]

DEBUG = True


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@crm.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "CRM"