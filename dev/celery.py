# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Establece el módulo de configuración de Django para Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dev.settings")

app = Celery("dev")

# Cargar configuración de Django en Celery
app.config_from_object("django.conf:settings", namespace="CELERY")

# Cargar tareas automáticamente de todas las apps instaladas
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
