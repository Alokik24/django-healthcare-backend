from django.db import models

from apps.doctors.models import Doctor
from apps.patients.models import Patient


class PatientDoctor(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="doctor_mappings",
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="patient_mappings",
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["patient", "doctor"],
                name="unique_patient_doctor",
            )
        ]
        ordering = ["-assigned_at"]

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"