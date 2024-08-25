from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StudentForm, DonorForm, IntermediaryForm, SchoolForm, EmployeeForm
from .models import School, Student, Donor, Intermediary, Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dataentry')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'User_pages/login.html')
        
    return render(request, 'login.html')
def dataentry(request):
    students = Student.objects.all()
    student_count = students.count()

    intermediaries = Intermediary.objects.all()
    intermediary_count = intermediaries.count()

    schools = School.objects.all()
    school_count = schools.count()

    context = {'students':students, 'student_count':student_count, 'intermediaries': intermediaries, 'intermediary_count': intermediary_count, 'schools': schools, 'school_count': school_count}
    return render(request, 'User_pages/dataentry.html', context)
def students(request):
    students = Student.objects.all().order_by('id')
    context = {'students':students}
    return render(request, 'lists/student_list.html', context)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'add_templates/add_student.html', {'form': form})
        
    form = StudentForm()
    return render(request, 'add_templates/add_student.html', {'form': form})
# student Profile
def student_profile(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'profiles/student_profile.html', context)
def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.info(request, 'Student Information Updated SuccessFully!')
            return redirect('students')
    context = {'form':form}
    return render(request, 'add_templates/add_student.html', context)

def intermediaries(request):
    intermediaries = Intermediary.objects.all()
    context = {'intermediaries':intermediaries}
    return render(request, 'lists/intermediary_list.html', context)
def add_intermediary(request):
    if request.method == 'POST':
        form = IntermediaryForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.info(request, 'Intermediary added Successfully!')
            return redirect('intermediaries')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'add_templates/add_intermediary.html', {'form': form})
        
    form = IntermediaryForm()
    return render(request, 'add_templates/add_intermediary.html', {'form': form})
def schools(request):
    schools = School.objects.all()
    context = {'schools':schools}
    return render(request, 'lists/school_list.html',context)
def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'School added Successfully!')
            return redirect('schools')
        else:
            messages.error(request, 'Invalid Form')
            return render(request, 'add_templates/add_school.html', {'form': form})
        
    form = SchoolForm()
    return render(request, 'add_templates/add_school.html', {'form':form})

def finance(request):
    employees = Employee.objects.all()
    employee_count = employees.count()

    donors = Donor.objects.all()
    donor_count = donors.count()

    context = {'employees':employees, 'employee_count':employee_count, 'donors': donors, 'donor_count': donor_count}
    return render(request, 'User_pages/finance.html', context)
#finance actions
def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.info(request, 'Donor added Successfully!')
            return redirect('donor_list')
        else:
            messages.error(request, 'Invalid Form')
            return render(request, 'add_templates/add_donor.html', {'form': form})
    form = DonorForm()
    return render(request, 'add_templates/add_donor.html', {'form': form})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Employee added Successfully!')
            return redirect('employee_list')
        else:
            messages.error(request, 'Invalid Form')
            return render(request, 'add_templates/add_employee.html', {'form': form})
    form = EmployeeForm()
    return render(request, 'add_templates/add_employee.html', {'form': form})
#finance pages access
def donor_list(request):
    donors = Donor.objects.all()
    context = {'donors':donors}
    return render(request, 'lists/donor_list.html', context)
def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request, 'lists/employee_list.html', context)

# logout function
def logout_view(request):
    logout(request)
    return redirect('login')