from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
# from datetime import timedelta
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

app = Celery('task_manager')
app.conf.enable_utc = False
# app.conf.update(timezone='Asia/Dhaka')
app.conf.update(timezone='Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'check-due-dates' : {
        'task': 'tasks.tasks.check_due_dates',
        'schedule': crontab(minute=1, hour=0), # schedule for everyday 12:01 am
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    #print('Request: {0!r}'.format(self.request))


'''Start Celery worker'''
# celery -A task_manager.celery worker --pool=solo -l info
# celery -A task_manager worker -l info
'''celery beat'''
# celery -A task_manager beat -l info