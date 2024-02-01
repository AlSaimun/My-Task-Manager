
from .models import Notification


def allnotifications(request):
    notifications = None
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[0:3]
    return {'notifications': notifications}