import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ele_make_iso.settings")
app = Celery("ele_make_iso")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()