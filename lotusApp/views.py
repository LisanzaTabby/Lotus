from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StudentForm, DonorForm, IntermediaryForm, EmployeeForm, SchoolForm,ExamResultsForm,ExamForm, FeesForm
from .models import Student, Donor, Intermediary, Employee, Exam, ExamResults, AcademicProgress,School,Fees
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from .filters import StudentFilter, IntermediaryFilter, DonorFilter,SchoolFilter,FeecommitmentFilter, DonorStudentFilter
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
@unauthenticated_user
def index(request):
    return render(request, 'index.html')
@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.groups.filter(name='Dataentry').exists():
                login(request, user)
                return redirect('dataentry')
            elif user.groups.filter(name='Finance').exists():
                login(request, user)
                return redirect('finance')
            elif user.groups.filter(name='Donor').exists():
                login(request, user)
                return redirect('donor_view')
            else:
                messages.info(request, 'You are not authorized to access this page!')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'User_pages/login.html')
        
    return render(request, 'login.html')
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def dataentry(request):
    students = Student.objects.all()
    student_count = students.count()

    schools = School.objects.all()
    schools_count = schools.count()

    intermediaries = Intermediary.objects.all()
    intermediary_count = intermediaries.count()
    context = {'students':students, 'student_count':student_count, 'intermediaries': intermediaries, 'intermediary_count': intermediary_count,'schools_count':schools_count}
    return render(request, 'User_pages/dataentry.html', context)

@login_required
@allowed_users(allowed_roles=['Dataentry', 'Finance'])
def students(request):
    students = Student.objects.all().order_by('id')
    myFilter = StudentFilter(request.POST, queryset=students)
    students = myFilter.qs

    is_finance = request.user.groups.filter(name='Finance').exists()
    is_dataentry = request.user.groups.filter(name='Dataentry').exists()
    context = {'students':students, 'myFilter': myFilter, 'is_finance':is_finance, 'is_dataentry':is_dataentry}
    return render(request, 'lists/student_list.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
    academicprogress = AcademicProgress.objects.filter(student=student).first()
    examresults = ExamResults.objects.filter(student=student).select_related('exam')
    donor_history = student.StudentDonorHistory.all().order_by('-year')
    is_dataentry = request.user.groups.filter(name='Dataentry').exists()
    context = {'student': student,'academicprogress':academicprogress,'examresults':examresults,'is_dataentry':is_dataentry, 'donor_history':donor_history}
    return render(request, 'profiles/student_profile.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry']) 
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
@allowed_users(allowed_roles=['Dataentry']) 
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.info(request, 'Student Deleted Successfully!')
        return redirect('students')
    context = {'student':student}
    return render(request, 'delete_templates/student_delete.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def intermediaries(request):
    intermediaries = Intermediary.objects.all().order_by('id')
    myFilter = IntermediaryFilter(request.POST, queryset=intermediaries)
    intermediaries = myFilter.qs
    context = {'intermediaries':intermediaries, 'myFilter':myFilter}
    return render(request, 'lists/intermediary_list.html', context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def add_intermediary(request):
    if request.method == 'POST':
        form = IntermediaryForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            messages.info(request, 'Intermediary added Successfully!')
            return redirect('intermediaries')
        else:
            print(form.errors)
            messages.error(request, 'Invalid form')
            return render(request, 'add_templates/add_intermediary.html', {'form': form})
        
    form = IntermediaryForm()
    return render(request, 'add_templates/add_intermediary.html', {'form': form})
@login_required
@allowed_users(allowed_roles=['Dataentry'])   
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
@allowed_users(allowed_roles=['Dataentry'])
def intermediary_delete(request, pk):
    intermediary = Intermediary.objects.get(id=pk)
    if request.method == 'POST':
        intermediary.delete()
        messages.info(request, 'Intermediary Deleted Successfully!')
        return redirect('intermediaries')
    context = {'intermediary':intermediary}
    return render(request, 'delete_templates/intermediary_delete.html', context)

@login_required
@allowed_users(allowed_roles=['Dataentry'])
def schools(request):
    schools = School.objects.all().order_by('id')
    myFilter = SchoolFilter(request.POST, queryset=schools)
    schools = myFilter.qs
    context = {'schools':schools, 'myFilter': myFilter}
    return render(request, 'lists/school_list.html',context)
@login_required
@allowed_users(allowed_roles=['Dataentry'])
def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'School added Successfully!')
            return redirect('schools')
        else:
            messages.error(request, form.errors)
            return render(request, 'add_templates/add_school.html', {'form': form})
        
    form = SchoolForm()
    return render(request, 'add_templates/add_school.html', {'form':form})
@login_required
@allowed_users(allowed_roles=['Dataentry'])
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
@allowed_users(allowed_roles=['Dataentry'])
def school_delete(request, pk):
    school = School.objects.get(id=pk)
    if request.method == 'POST':
        school.delete()
        messages.info(request, 'School Deleted Successfully!')
        return redirect('schools')
    context = {'school':school}
    return render(request, 'delete_templates/school_delete.html', context)

@login_required
@allowed_users(allowed_roles=['Finance'])
def finance(request):
    employees = Employee.objects.all()
    employee_count = employees.count()

    donors = Donor.objects.all()
    donor_count = donors.count()
    students = Student.objects.all()
    student_count = students.count()

    fees = Fees.objects.all()
    total_committed = fees.aggregate(total_committed=Sum('committed_amount'))['total_committed'] or 0
    total_contributed = fees.aggregate(total_contributed=Sum('contributed_amount'))['total_contributed'] or 0


    context = {'employees':employees, 'employee_count':employee_count, 'donors': donors, 'donor_count': donor_count,'students':students,'student_count':student_count,'fees':fees,'total_committed':total_committed,'total_contributed':total_contributed}
    return render(request, 'User_pages/finance.html', context)
#finance actions
#finance pages access
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@allowed_users(allowed_roles=['Finance'])
def donor_list(request):
    donors = Donor.objects.all().order_by('id')
    myFilter = DonorFilter(request.POST, queryset=donors)
    donors = myFilter.qs

    context = {'donors':donors, 'myFilter': myFilter}
    return render(request, 'lists/donor_list.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@allowed_users(allowed_roles=['Finance'])
def donor_delete(request, pk):
    donor = Donor.objects.get(id=pk)
    if request.method == 'POST':
        donor.delete()
        messages.info(request, 'Donor Deleted Successfully!')
        return redirect('donor_list')
    context = {'donor':donor}
    return render(request, 'delete_templates/donor_delete.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
def add_fee_commitment(request):
    if request.method == 'POST':
        form = FeesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donor Fee Commitment Saved Successfully!')
            return redirect('donor_commitment_list')
        else:
            messages.error(request, 'Invalid Form')
            return render(request, 'add_templates/add_fee_commitment.html',{'form':form})
    form=FeesForm()
    return render(request, 'add_templates/add_fee_commitment.html',{'form':form})
@login_required
@allowed_users(allowed_roles=['Finance'])
def donor_commitment_list(request):
    fees = Fees.objects.all().order_by('id')
    myFilter = FeecommitmentFilter(request.POST, queryset=fees)
    fees = myFilter.qs
    context = {'fees':fees, 'myFilter': myFilter}
    return render(request, 'lists/donor_commitment_list.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
def edit_donor_commitment(request,pk):
    fee = Fees.objects.get(id=pk)
    form = FeesForm(instance=fee)
    if request.method == 'POST':
        form = FeesForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            messages.info(request, 'Donor Fee Commitment Updated SuccessFully!')
            return redirect('donor_commitment_list')
    context = {'form':form}    
    return render(request, 'add_templates/add_fee_commitment.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
def delete_donor_commitment(request,pk):
    fee = Fees.objects.get(id=pk)
    if request.method == 'POST':
        fee.delete()
        messages.info(request, 'Donor Fee Commitment Deleted Successfully!')
        return redirect('donor_commitment_list')
    context = {'fee':fee}
    return render(request, 'delete_templates/delete_donor_commitment.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@allowed_users(allowed_roles=['Finance'])
def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    context = {'employees':employees}
    return render(request, 'lists/employee_list.html', context)
@login_required
@allowed_users(allowed_roles=['Finance'])
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
@allowed_users(allowed_roles=['Finance'])
def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        messages.info(request, 'Employee Deleted Successfully!')
        return redirect('employee_list')
    context = {'employee':employee}
    return render(request, 'delete_templates/employee_delete.html', context)

@login_required
@allowed_users(allowed_roles=['Donor'])
def donor_view(request):
    students = Student.objects.filter(donor=request.user)
    student_count = students.count()
    #commitments = Fees.objects.filter(donor=request.user)

    # Debugging
    #for commitment in commitments:

       # print(f"Commitment ID: {commitment.id}, Amount: {commitment.amount}")

    context = {'students':students, 'student_count':student_count}
    return render(request, 'User_pages/donor.html', context)
@login_required
@allowed_users(allowed_roles=['Donor'])
def donor_specific_students(request):
    students = Student.objects.filter(donor=request.user)
    myFilter = DonorStudentFilter(request.POST, queryset=students)
    students = myFilter.qs
    context = {'students':students, 'myFilter': myFilter}
    return render(request, 'lists/donor_specific_students.html', context)
# student updation actions
def update_academic_progress(request, pk):
    student = get_object_or_404(Student, id=pk)

    # Get the academic progress instance or create one if it doesn't exist
    progress, created = AcademicProgress.objects.get_or_create(student=student)

    if request.method == 'POST':
        try:
            year = int(request.POST.get('year'))
            class_level = request.POST.get('class_level')

            # Make sure the class_level is valid before proceeding
            if not class_level:
                messages.error(request, 'Class level is required.')
                return render(request, 'add_templates/add_academic_progress.html', {'progress': progress, 'student': student})

            progress.update_progress(year, class_level)
            messages.success(request, 'Academic Progress saved successfully!')
            return redirect('student_profile', pk=pk)
        except ValueError:
            messages.error(request, 'Invalid input for year.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'add_templates/add_academic_progress.html', {'progress': progress, 'student': student})
def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam Added Successfully!')
            return redirect('exam_list')
    form = ExamForm()
    context = {'form':form}
    return render(request, 'add_templates/add_exam.html',context)
def exams(request):
    exams = Exam.objects.all().order_by('id')
    context = {'exams':exams}
    return render(request,'lists/exam_list.html', context)
def update_exam_results(request, pk):
    student = Student.objects.get(id=pk)
    form = ExamResultsForm(instance=student)
    if request.method == 'POST':
        form = ExamResultsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Exam Results Updated SuccessFully!')
            return redirect('student_profile')
    context = {'form':form,'student':student}
    return render(request, 'add_templates/add_exam_results.html', context)
# logout function
def logout_view(request):
    logout(request)
    return redirect('login')
# Password reset
def forgot_password(request):
    return HttpResponse("Feature is Under Development......")