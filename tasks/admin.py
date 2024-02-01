from django.contrib import admin

# local import
from .models import Task, Image,  Notification
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'priority', 'due_date', 'is_completed', 'is_notified', 'created_at', 'updated_at']
    list_filter = ('due_date', 'created_at', 'priority', 'is_completed')
    ordering = ('-priority',) # ordering : High - Medium - Low
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['task', 'image']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'type']