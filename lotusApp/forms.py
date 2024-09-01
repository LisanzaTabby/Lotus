from .models import Student, Donor, Intermediary, Employee, AcademicProgress, Exam, ExamResults
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
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['date_added']
class AcademicProgressForm(ModelForm):
    class Meta:
        model = AcademicProgress
        fields = '__all__'
class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
class ExamResultsForm(ModelForm):
    class Meta:
        model = ExamResults
        fields = '__all__'

