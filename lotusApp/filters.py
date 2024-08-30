import django_filters
from django_filters import *
from .models import *

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
    POSITION=(
        ('Continuing', 'Continuing'),
        ('Graduate', 'Graduate'),
        ('Undergraduate', 'Undergraduate'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),   
    )
    studentName = django_filters.CharFilter(lookup_expr='icontains', label='Student Name')
    school = django_filters.CharFilter(lookup_expr='icontains', label='School')
    position = django_filters.ChoiceFilter(choices=POSITION, label='Position') 
    level = django_filters.ChoiceFilter(choices=LEVELofSUPPORT, label='Level of Support')
    class Meta:
        model = Student
        fields = ['gender']
