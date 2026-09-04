from django.urls import path

from .views import (
    MappingDeleteView,
    MappingListCreateView,
    PatientMappingListView,
)


urlpatterns = [
    path(
        "mappings/",
        MappingListCreateView.as_view(),
        name="mapping-list-create",
    ),
    path(
        "mappings/patient/<int:patient_id>/",
        PatientMappingListView.as_view(),
        name="patient-mappings",
    ),
    path(
        "mappings/<int:pk>/",
        MappingDeleteView.as_view(),
        name="mapping-delete",
    ),
]