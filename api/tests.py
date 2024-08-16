from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Department, PatientRecord

class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(
            name='Cardiology',
            diagnostics='Heart-related diagnostics',
            location='Building A',
            specialization='Heart Diseases'
        )

    def test_department_creation(self):
        self.assertEqual(self.department.name, 'Cardiology')

class PatientRecordModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.department = Department.objects.create(
            name='Cardiology',
            diagnostics='Heart-related diagnostics',
            location='Building A',
            specialization='Heart Diseases'
        )
        self.patient_record = PatientRecord.objects.create(
            patient=self.user,
            diagnostics='Normal ECG',
            observations='Healthy',
            treatments='No treatment required',
            department=self.department,
            misc='N/A'
        )

    def test_patient_record_creation(self):
        self.assertEqual(self.patient_record.patient.username, 'testuser')
        self.assertEqual(self.patient_record.department.name, 'Cardiology')
