from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

PRIORITY_CHOICES = (
    ('3', 'High'),
    ('2', 'Medium'),
    ('1', 'Low'),
)

NOTIFICATION_TYPE = (
    ('Start', 'Start'), # start task for send notification
    ('End', 'End'), # end task for send notification
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    description = models.TextField(max_length=255, null= True, blank = True)
    priority = models.CharField(max_length = 10, choices = PRIORITY_CHOICES)
    due_date = models.DateField()
    is_completed = models.BooleanField(default = False) 
    is_notified = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self) -> str:
        return self.title
    
    def get_priority(self):
        '''this function for showing priority in frontend'''
        if self.priority == '3':
            return "High"
        elif self.priority == '2':
            return "Medium"
        else:
            return "Low"

class Image(models.Model):
    task = models.ForeignKey(Task, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/tasks')


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    type = models.CharField(max_length = 10, choices = NOTIFICATION_TYPE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.task.title
    
    def full_message(self):
        if self.type == 'Start':
            return f"You have started {self.task.title} from today"
        return f"Your due date is over please check the task"