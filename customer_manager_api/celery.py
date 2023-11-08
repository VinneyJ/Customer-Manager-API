import os

from celery import Celery
from django.conf import settings

# TODO: we can change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "customer_manager_api.settings.local")

app = Celery("customer_manager_api")    

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)