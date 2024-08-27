import django_filters
from django_filters import *
from .models import *

class StudentFilter(django_filters.FilterSet):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = django_filters.CharFilter(lookup_expr='icontains', label='Student Name')
    gender = django_filters.ChoiceFilter(choices=GENDER, label='Gender')
    school = django_filters.ModelMultipleChoiceFilter(queryset=School.objects.all(), label='School')
    intermediary = django_filters.ModelMultipleChoiceFilter(queryset=Intermediary.objects.all(), label='Intermediary')
    donor = django_filters.ModelMultipleChoiceFilter(queryset=Donor.objects.all(), label='Donor')
    class Meta:
        model = Student
        fields = ['gender']

