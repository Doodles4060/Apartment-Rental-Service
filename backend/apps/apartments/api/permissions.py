from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owner of an Apartment to delete or edit it.
    """
    message = 'You must be the owner of this apartment to edit or delete it.'

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.owner == request.user