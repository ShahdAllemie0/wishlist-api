from rest_framework.permissions import BasePermission

class IsStaffOrUser(BasePermission):
    message = "You must be staff or the user who added the item"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.added_by == request.user):
            return True
        else:
            return False
