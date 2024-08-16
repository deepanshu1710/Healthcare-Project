from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_doctor

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_patient

class IsOwnerOrDoctor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user or request.user.is_doctor and request.user.department == obj.department
