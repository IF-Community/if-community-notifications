from rest_framework.permissions import BasePermission
from rest_framework_api_key.permissions import HasAPIKey

class IsAuthenticatedAndIsAdminUserOrHasAPIKey(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and
            request.user and request.user.is_staff or
            HasAPIKey().has_permission(request, view)
        )
