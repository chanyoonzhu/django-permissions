from rest_framework import permissions

class IsPurchaserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # READ ONLY is allowed for GETS
        if request.method in permissions.SAFE_METHODS: # methods not making any changes such as GET
            return True

        return obj.purchaser == request.user