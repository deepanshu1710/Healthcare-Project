from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.TextField()
    location = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

class PatientRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient_records')
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatments = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    misc = models.TextField()

    def __str__(self):
        return f'Record {self.record_id} for {self.patient.username}'
