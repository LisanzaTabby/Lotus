from .models import Student, Donor, Intermediary, School
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['date_added']

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        exclude = ['date_added']

class IntermediaryForm(ModelForm):
    class Meta:
        model = Intermediary
        fields = '__all__'
        exclude = ['date_added']

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        exclude = ['date_added']
