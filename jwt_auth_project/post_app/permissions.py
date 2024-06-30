from rest_framework import permissions


class IsAuthenticatedOrAdminOnly(permissions.BasePermission):
    def has_premission(self, request, view):
        return bool( request.user and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_staff)