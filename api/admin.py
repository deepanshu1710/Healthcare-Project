from django.contrib import admin
from .models import Department, PatientRecord, CustomUser

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'specialization')

@admin.register(PatientRecord)
class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'patient', 'created_date', 'department')
    search_fields = ('patient__username', 'department__name')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_doctor', 'is_patient', 'department')
    search_fields = ('username', 'email')
