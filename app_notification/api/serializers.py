from rest_framework import serializers

from ..models import Notification, Users

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'sender', 'type_message', 'created_at', 'read']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'user', 'profile_name', 'email']