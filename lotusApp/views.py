from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StudentForm, DonorForm, IntermediaryForm, SchoolForm, EmployeeForm
from .models import School, Student, Donor, Intermediary, Employee
from django.contrib.auth.decorators import login_required
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
@login_required
def dataentry(request):
    students = Student.objects.all()
    student_count = students.count()

    intermediaries = Intermediary.objects.all()
    intermediary_count = intermediaries.count()

    schools = School.objects.all()
    school_count = schools.count()

    context = {'students':students, 'student_count':student_count, 'intermediaries': intermediaries, 'intermediary_count': intermediary_count, 'schools': schools, 'school_count': school_count}
    return render(request, 'User_pages/dataentry.html', context)

@login_required
def students(request):
    students = Student.objects.all().order_by('id')
    context = {'students':students}
    return render(request, 'lists/student_list.html', context)
@login_required
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
@login_required
def student_profile(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'profiles/student_profile.html', context)
@login_required
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
@login_required
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.info(request, 'Student Deleted Successfully!')
        return redirect('students')
    context = {'student':student}
    return render(request, 'delete_templates/student_delete.html', context)
@login_required
def intermediaries(request):
    intermediaries = Intermediary.objects.all().order_by('id')
    context = {'intermediaries':intermediaries}
    return render(request, 'lists/intermediary_list.html', context)
@login_required
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
@login_required
def edit_intermediary(request, pk):
    intermediary = Intermediary.objects.get(id=pk)
    form = IntermediaryForm(instance=intermediary)
    if request.method =='POST':
        form = IntermediaryForm(request.POST,instance=intermediary)
        if form.is_valid():
            form.save()
            messages.info(request, 'Intermediary Information Updated SuccessFully!')
            return redirect('intermediaries')
    context = {'form':form}
    return render(request, 'add_templates/add_intermediary.html', context)
@login_required
def intermediary_delete(request, pk):
    intermediary = Intermediary.objects.get(id=pk)
    if request.method == 'POST':
        intermediary.delete()
        messages.info(request, 'Intermediary Deleted Successfully!')
        return redirect('intermediaries')
    context = {'intermediary':intermediary}
    return render(request, 'delete_templates/intermediary_delete.html', context)
@login_required
def schools(request):
    schools = School.objects.all()
    context = {'schools':schools}
    return render(request, 'lists/school_list.html',context)
@login_required
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
@login_required
def edit_school(request, pk):
    school = School.objects.get(id=pk)
    form = SchoolForm(instance=school)
    if request.method =='POST':
        form = SchoolForm(request.POST,instance=school)
        if form.is_valid():
            form.save()
            messages.info(request, 'School Information Updated SuccessFully!')
            return redirect('schools')
    context = {'form':form}
    return render(request, 'add_templates/add_school.html', context)
@login_required
def school_delete(request, pk):
    school = School.objects.get(id=pk)
    if request.method == 'POST':
        school.delete()
        messages.info(request, 'School Deleted Successfully!')
        return redirect('schools')
    context = {'school':school}
    return render(request, 'delete_templates/school_delete.html', context)
@login_required
def finance(request):
    employees = Employee.objects.all()
    employee_count = employees.count()

    donors = Donor.objects.all()
    donor_count = donors.count()

    context = {'employees':employees, 'employee_count':employee_count, 'donors': donors, 'donor_count': donor_count}
    return render(request, 'User_pages/finance.html', context)
#finance actions
#finance pages access
@login_required
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
@login_required
def donor_list(request):
    donors = Donor.objects.all()
    context = {'donors':donors}
    return render(request, 'lists/donor_list.html', context)
@login_required
def edit_donor(request, pk):
    donor = Donor.objects.get(id=pk)
    form = DonorForm(instance=donor)
    if request.method =='POST':
        form = DonorForm(request.POST,instance=donor)
        if form.is_valid():
            form.save()
            messages.info(request, 'Donor Information Updated SuccessFully!')
            return redirect('donor_list')
    context = {'form':form}
    return render(request, 'add_templates/add_donor.html', context)
@login_required
def donor_delete(request, pk):
    donor = Donor.objects.get(id=pk)
    if request.method == 'POST':
        donor.delete()
        messages.info(request, 'Donor Deleted Successfully!')
        return redirect('donor_list')
    context = {'donor':donor}
    return render(request, 'delete_templates/donor_delete.html', context)
@login_required
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
@login_required
def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    context = {'employees':employees}
    return render(request, 'lists/employee_list.html', context)
@login_required
def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method =='POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            messages.info(request, 'Employee Information Updated SuccessFully!')
            return redirect('employee_list')
    context = {'form':form}
    return render(request, 'add_templates/add_employee.html', context)
@login_required
def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        messages.info(request, 'Employee Deleted Successfully!')
        return redirect('employee_list')
    context = {'employee':employee}
    return render(request, 'delete_templates/employee_delete.html', context)
# logout function
def logout_view(request):
    logout(request)
    return redirect('login')