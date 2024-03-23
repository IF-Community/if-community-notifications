from django.contrib import admin
from django.urls import path, include
from app_notification.views import NotificationViewSet

# DRF
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notifications', NotificationViewSet, basename='notifications')

# DRF Spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF Spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

] + router.urls
