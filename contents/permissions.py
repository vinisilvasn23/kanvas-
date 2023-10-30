from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class AccessContentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        return request.user.is_superuser


def check_content_permission(course, user):
    id_user = user.id
    if course.students.filter(id=id_user).exists() or user.is_superuser:
        return True
    raise PermissionDenied()
