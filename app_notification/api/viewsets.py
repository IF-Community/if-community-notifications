from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_api_key.permissions import HasAPIKey

from app_notification.api.serializers import NotificationSerializer, UsersSerializer
from app_notification.models import Notification, Users
from app_notification.permissions import IsAuthenticatedAndIsAdminUserOrHasAPIKey

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticatedAndIsAdminUserOrHasAPIKey]


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticatedAndIsAdminUserOrHasAPIKey]
