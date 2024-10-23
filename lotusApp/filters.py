import django_filters
from django_filters import *
from .models import *
'''
class StudentFilter(django_filters.FilterSet):
    LEVELofSUPPORT = (
        ('PrimaryOnly', 'PrimaryOnly'),
        ('Primary&Secondary', 'Primary&Secondary'),
        ('Primary&Secondary&Tertiary', 'Primary&Secondary&Tertiary'),
        ('Secondary&tertiary', 'Secondary&tertiary'),
        ('TertiaryOnly', 'TertiaryOnly'),
        ('SecondaryOnly', 'SecondaryOnly'),
        ('Primary&Tertiary', 'Primany&Tertiary'),
    )
    studentName = django_filters.CharFilter(lookup_expr='icontains', label='Student Name')
    donor = django_filters.ModelChoiceFilter(queryset=User.objects.all(), label='Donor')
    intermediary = django_filters.ModelChoiceFilter(queryset=Intermediary.objects.all(), label='Intermediary')
    primary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Primary School')
    secondary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Secondary School')
    tertiary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Tertiary Institution')
    class Meta:
        model = Student
        fields = ['gender']

class StudentDonorHistoryFilter(django_filters.FilterSet):
    studentName = django_filters.CharFilter(lookup_expr='icontains', label='Student Name')
    donor = django_filters.ModelChoiceFilter(queryset=User.objects.all(), label='Donor')
    class Meta:
        model = StudentDonorHistory
        fields = ['year']
class DonorStudentFilter(django_filters.FilterSet):
    studentName = django_filters.CharFilter(lookup_expr='icontains', label='Student Name')  
    primary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Primary School')
    secondary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Secondary School')
    tertiary_school = django_filters.ModelChoiceFilter(queryset=School.objects.all(), label='Tertiary Institution')
    class Meta:
        model = Student
        fields = ['gender']
class IntermediaryFilter(django_filters.FilterSet):
    class Meta:
        model = Intermediary
        fields = ['intermediaryName', 'location']

class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ['donorName']
class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ['schoolName']

class FeecommitmentFilter(django_filters.FilterSet):
    class Meta:
        model = Fees
        fields = ['donor','year']
'''