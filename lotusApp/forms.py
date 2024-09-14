from .models import Student, Donor, Intermediary, Employee, Exam, ExamResults, School, Fees
from django.forms import ModelForm
from django import forms

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
class FeesForm(ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'
        exclude = ['date_added']

    def clean(self):
        cleaned_data = super().clean()
        donor = cleaned_data.get('donor')
        year = cleaned_data.get('year')

        if Fees.objects.filter(donor=donor, year=year).exists():
            raise forms.ValidationError(f"Fees record for {donor} in year {year} already exists.")
        
        return cleaned_data
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
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['date_added']
'''
class AcademicProgressForm(ModelForm):
    class Meta:
        model = AcademicProgress
        fields = '__all__'
'''
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
class ExamResultsForm(ModelForm):
    class Meta:
        model = ExamResults
        fields = '__all__'
