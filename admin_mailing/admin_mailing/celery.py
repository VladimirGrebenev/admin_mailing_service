import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_mailing.settings")
celery_app = Celery("admin_sender")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


# Здесь можно указать интервал выполнения задачи инициализации рассылок
celery_app.conf.beat_schedule = {
    'process_dispatches': {
        'task': 'main_app.tasks.process_dispatches',
        'schedule': timedelta(minutes=1),
    },
}