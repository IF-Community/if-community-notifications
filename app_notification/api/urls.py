from rest_framework import routers

from app_notification.api.viewsets import NotificationViewSet, UsersViewSet

router = routers.SimpleRouter()
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'users', UsersViewSet, basename='users')