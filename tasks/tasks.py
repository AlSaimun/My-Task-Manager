from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Task, Notification
from datetime import date
from channels.db import database_sync_to_async

@shared_task(bind = True)
def check_due_dates(self):
    print("Task Start...........")
    tasks = Task.objects.filter(due_date__lt=date.today(), is_notified=False, is_completed=False)
    for task in tasks:
        channel_layer = get_channel_layer()
        notification = Notification.objects.create(user = task.user, task = task, type = "End")
        async_to_sync(channel_layer.group_send)(task.user.username, {
            'type': 'send.notification',
            'message': notification.full_message(),
            'task' : task.title,
        })
        task.is_notified = True
        task.save()
    return "Done"


@shared_task(bind = True)
def test_task(self):
    for i in range(10):
        print(i)
    return "Done"