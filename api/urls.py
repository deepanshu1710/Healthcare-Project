from django.urls import path
from .views import DepartmentListCreateView, PatientRecordListCreateView, UserListCreateView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('patient_records/', PatientRecordListCreateView.as_view(), name='patient-record-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
]
