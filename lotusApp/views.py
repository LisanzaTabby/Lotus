from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StudentForm, DonorForm, IntermediaryForm, SchoolForm

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
    return render(request, 'User_pages/dataentry.html')
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
            form.save()
            return redirect('intermediaries')
        else:
            messages.error(request, 'Invalid form')
            return render(request, 'add_templates/add_intermediary.html', {'form': form})
        
    form = IntermediaryForm()
    return render(request, 'add_templates/add_intermediary.html', {'form': form})
# logout function
def logout_view(request):
    logout(request)
    return redirect('login')