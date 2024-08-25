from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StudentForm, DonorForm, IntermediaryForm, SchoolForm
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
    context = {}
    return render(request, 'lists/student_list.html', context)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'add_templates/add_student.html', {'form': form})
        
    form = StudentForm()
    return render(request, 'add_templates/add_student.html', {'form': form})

def intermediaries(request):
    context = {}
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
            errors = form.errors
            messages.error(request, errors)
            return render(request, 'add_templates/add_intermediary.html', {'form': form})
        
    form = IntermediaryForm()
    return render(request, 'add_templates/add_intermediary.html', {'form': form})
def schools(request):
    context = {}
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
# logout function
def logout_view(request):
    logout(request)
    return redirect('login')