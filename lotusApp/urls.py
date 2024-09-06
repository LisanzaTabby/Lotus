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
    path('deletestudent/<str:pk>/', views.student_delete, name='deletestudent'),
    path('update_academic_progress/<str:pk>/', views.update_academic_progress, name='update_academic_progress'),
    path('exam/', views.exams, name='exam_list'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('update_exam_results/<str:pk>/', views.update_exam_results, name='update_exam_results'),
    path('intermediaries/', views.intermediaries, name='intermediaries'),
    path('add_intermediary/', views.add_intermediary, name='add_intermediary'),
    path('editintermediary/<str:pk>/', views.edit_intermediary, name='editintermediary'),
    path('deleteintermediary/<str:pk>/', views.intermediary_delete, name='deleteintermediary'),
    path('schools/', views.schools, name='schools'),
    path('add_school/', views.add_school, name='add_school'),
    path('edit_school/<str:pk>/', views.edit_school, name='edit_school'),
    path('delete_school/<str:pk>/', views.school_delete, name='delete_school'),
    path('finance/', views.finance, name='finance'),
    path('donor_list/', views.donor_list, name='donor_list'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('edit_donor/<str:pk>/', views.edit_donor, name='edit_donor'),
    path('delete_donor/<str:pk>/', views.donor_delete, name='delete_donor'),
    path('add_fee_commitment/', views.add_fee_commitment, name= 'add_fee_commitment'),
    path('edit_donor_commitment/<str:pk>/', views.edit_donor_commitment, name='edit_donor_commitment'),
    path('delete_donor_commitment/<str:pk>/', views.delete_donor_commitment, name='delete_fee_commitment'),
    path('donor_commitment_list/', views.donor_commitment_list, name='donor_commitment_list'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<str:pk>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<str:pk>/', views.employee_delete, name='delete_employee'),
    path('donor_view/', views.donor_view, name='donor_view'),
    path('donor_specific_students/', views.donor_specific_students, name='donor_specific_students'),
    path('logout/', views.logout_view, name='logout'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
]