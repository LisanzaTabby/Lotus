from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('dataentry/', views.dataentry, name='dataentry'),
    path('students/', views.students, name='students'),
    path('add_student/', views.add_student, name='add_student'),
    path('intermediaries/', views.intermediaries, name='intermediaries'),
    path('add_intermediary/', views.add_intermediary, name='add_intermediary'),
    path('logout/', views.logout_view, name='logout'),
]