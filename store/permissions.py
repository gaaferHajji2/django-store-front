from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  # type: ignore
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsCustomerServiceOnly(permissions.DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

class CanViewHistory(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('store.view_history')
