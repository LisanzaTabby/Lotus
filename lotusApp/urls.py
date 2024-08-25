from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('dataentry/', views.dataentry, name='dataentry'),
    path('students/', views.students, name='students'),
    path('add_student/', views.add_student, name='add_student'),
    path('studentprofile/<str:pk>/', views.student_profile, name='student_profile'),
    path('edit_student/<str:pk>/', views.edit_student, name='edit_student'),
    path('intermediaries/', views.intermediaries, name='intermediaries'),
    path('add_intermediary/', views.add_intermediary, name='add_intermediary'),
    path('schools/', views.schools, name='schools'),
    path('add_school/', views.add_school, name='add_school'),
    path('finance/', views.finance, name='finance'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('donor_list/', views.donor_list, name='donor_list'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('logout/', views.logout_view, name='logout'),
]