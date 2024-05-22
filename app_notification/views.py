from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer, UsersSerializer
from .models import Notification, Users

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, )
