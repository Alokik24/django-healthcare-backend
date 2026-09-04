from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import PatientDoctor
from .serializers import PatientDoctorSerializer
from apps.patients.models import Patient


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctor.objects.select_related(
            "patient",
            "doctor",
        )

    def perform_create(self, serializer):
        serializer.save()


class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [IsAuthenticated]

    queryset = PatientDoctor.objects.select_related(
        "patient",
        "doctor",
    )


class PatientMappingListView(generics.ListAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient = get_object_or_404(
            Patient,
            pk=self.kwargs["patient_id"],
        )

        return PatientDoctor.objects.filter(
            patient=patient
        ).select_related(
            "patient",
            "doctor",
        )