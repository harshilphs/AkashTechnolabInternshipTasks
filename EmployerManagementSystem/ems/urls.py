from django.contrib import admin
from django.urls import path

from ems import views

urlpatterns = [
    path('', views.login),
    path('registration/', views.register, name="registration"),
    path('employerDashboard/', views.dashboard, name="employerDashboard"),
    path('employerDashboard/empDataForm', views.emp_data_form,name="empDataForm"),
    path('employerDashboard/editEmployer/<int:id>/', views.emp_data_edit, name="editEmployer"),
    path('employerDashboard/deleteEmployer/<int:id>/', views.emp_data_delete, name="deleteEmployer"),
    path('logout/', views.logout, name="logout")
]