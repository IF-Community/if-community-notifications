from rest_framework import viewsets
from .serializers import NotificationSerializer
from .models import Notification

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
