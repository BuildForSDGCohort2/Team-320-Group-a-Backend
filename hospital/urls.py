from django.urls import path
from . import views


urlpatterns = [
    path('', views.HospitalListAPIView.as_view(), name="hospital"),
    path('Create&ViewPatientHealthBill/', views.PatientsHospitalListView.as_view(), name="Create&ViewPatientHealthBill"),
    path('patientCreate/', views.PatientsListView.as_view(), name="patientCreate&list"),
    path('PatientHealthBillDetails/<str:code_no>/', views.PatientHospitalDetails.as_view(), name="PatientHealthBilldetails"),
    path('patientDetails/<str:code_no>/', views.PatientDetails.as_view(), name="patientdetails")
]
