from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id', 'task_name', 'start_day')
