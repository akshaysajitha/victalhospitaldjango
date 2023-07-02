from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('home', views.home, name='home'),
path('adminlogin',views.adminlogin,name='adminlogin'),
path('adminloginvalidater',views.adminloginvalidater,name='adminloginvalidater'),
path('adminhome',views.adminhome,name='adminhome'),
path('patientlogin',views.patientlogin,name='patientlogin'),
path('patientregister',views.patientregister,name='patientregister'),
path('doctorlogin',views.doctorlogin,name='doctorlogin'),
path('doctorregister',views.doctorregister,name='doctorregister'),
path('doctorregesterform',views.doctorregesterform,name='doctorregesterform'),
path('patientregistervalidater',views.patientregistervalidater,name='patientregistervalidater'),
path('patientloginvalidater',views.patientloginvalidater,name='patientloginvalidater'),
path('doctorloginvalidater',views.doctorloginvalidater,name='doctorloginvalidater'),
path('doctorhome',views.doctorhome,name='doctorhome'),
path('admindoctorrequest',views.admindoctorrequest,name='admindoctorrequest'),
path('adminapprovedoctor',views.adminapprovedoctor,name='adminapprovedoctor'),
path('adminselecteddoctorview',views.adminselecteddoctorview,name='adminselecteddoctorview'),
path('admindeletedoctor',views.admindeletedoctor, name='admindeletedoctor'), 
]
