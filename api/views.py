from rest_framework import generics, permissions
from .models import Department, PatientRecord, CustomUser
from .serializers import DepartmentSerializer, PatientRecordSerializer, UserSerializer
from .permissions import IsDoctor, IsPatient, IsOwnerOrDoctor

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

class PatientRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor:
            return PatientRecord.objects.filter(department=user.department)
        elif user.is_patient:
            return PatientRecord.objects.filter(patient=user)
        return PatientRecord.objects.none()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
