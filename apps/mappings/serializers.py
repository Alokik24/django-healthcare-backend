from rest_framework import serializers

from .models import PatientDoctor


class PatientDoctorSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True,
    )
    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True,
    )

    class Meta:
        model = PatientDoctor
        fields = [
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "assigned_at",
        ]
        read_only_fields = [
            "id",
            "patient_name",
            "doctor_name",
            "assigned_at",
        ]

    def validate(self, attrs):
        patient = attrs["patient"]
        doctor = attrs["doctor"]

        if PatientDoctor.objects.filter(
            patient=patient,
            doctor=doctor,
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return attrs