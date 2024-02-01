from django.urls import path

# local import
from .views import *

urlpatterns = [
    path('filter/<str:category>/', FilterView.as_view(), name= 'filter-task'),
    path('create-task/', TaskCreateView.as_view(), name= 'create-task'),
    path('delete/<int:id>/', TaskDeleteView.as_view(), name= 'delete-task'),
    path('confirm-delete/<int:id>/', TaskDeleteView.as_view(), name= 'confirm-delete-task'),
    path('task-details/<int:pk>/', TaskDetailView.as_view(), name= 'task-details'),
    path('update-task/<int:id>/', TaskUpdateView.as_view(), name= 'update-task'),
    path('delete-image/<int:pk>/', ImageDeleteView.as_view(), name='delete-image'),
    path('delete-image/<int:pk>/', ImageDeleteView.as_view(), name='delete-image-conf'),
    path('search/', TaskSearchView.as_view(), name='task-search'),


    path('api/task/<int:pk>/', TaskAPIView.as_view()),
    path('api/task/', TaskAPIView.as_view(), name='task-api'),
]
