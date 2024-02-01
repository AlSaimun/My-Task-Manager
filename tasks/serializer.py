from rest_framework import serializers


# local import
from . models import Task, Image
from django.conf import settings

class ImageSerializer(serializers.ModelSerializer):
    '''Image serializer'''
    class Meta:
        model = Image
        fields = ('image',)


class TaskSerializer(serializers.ModelSerializer):
    '''task serializer'''
    images = ImageSerializer(many = True, read_only = True)
    class Meta:
        model = Task
        fields = ('id','user', 'title', 'description', 'priority', 'due_date', 'is_completed', 'images')

    def get_user(self, obj):
        return obj.user.username if obj.user else None
    
    def to_representation(self, instance):
        '''for represent username'''
        data = super().to_representation(instance)
        data['user'] = self.get_user(instance)
        return data
    