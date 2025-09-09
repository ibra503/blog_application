from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #GET, HEAD, OPTIONS are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        #  only the author can edit/delete
        return obj.author == request.user
