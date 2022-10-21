from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project',broker='redis://127.0.0.1:6379')
# app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')
# app = Celery('myapp', broker='amqp://guest:guest@172.17.0.3:5672//')

# app.conf.update(
#     result_backend='db+sqlite:///django-db')

# Celery Beat Settings
# app.conf.beat_schedule = {
#     'send-mail-every-day-at-7': {
#         'task': 'send_mail_app.tasks.send_mail_func',
#         'schedule': crontab(hour=12, minute=37,),# day_of_month=19, month_of_year = 6,
#     }
# }

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')