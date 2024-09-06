from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Intermediary(models.Model):
    LOCATION = (
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Kitale', 'Kitale'),
        ('Eldoret', 'Eldoret'),
        ('Nakuru', 'Nakuru'),
        ('Kajiado', 'Kajiado'),
        ('Laikipia', 'Laikipia'),
    )

    intermediaryName= models.CharField(max_length=100)
    intermediaryEmail = models.EmailField(max_length=100, unique=True)
    intermediaryPhone = models.CharField(max_length=10, unique=True)
    contactPerson = models.CharField(max_length=100, null=True, blank=True) 
    location = models.CharField(max_length=10, choices=LOCATION)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.intermediaryName}'
    
class Donor(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, null=True)
    donorName = models.CharField(max_length=100)
    donorEmail = models.EmailField(max_length=100, unique=True)
    donorPhone = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.donorName}'
    def total_committed_fees(self):
        return self.fees_amounts.aggregate(total_committed_fees=Sum('committed_amount'))['total_committed_fees'] or 0
    def total_contributed_fees(self):
        return self.fees_amounts.aggregate(total_contributed_fees=Sum('contributed_amount'))['total_contributed_fees'] or 0
    def cumulative_fees(self, start_year, end_year):
        fees = self.fees_amounts.all()
        if start_year and end_year:
            fees = fees.filter(year__gte=start_year, year__lte=end_year)
        total_fees = fees.aggregate(
            total_committed_amount = Sum('committed_amount'),
            total_contributed_amount = Sum('contributed_amount')
        )
        return {
            'total_committed_amount':total_fees['total_committed_amount'] or 0,
            'total_contributed_amount': total_fees['total_contributed_amount'] or 0
        }
class Fees(models.Model):
    donor = models.ForeignKey(Donor, related_name='fees_amounts', on_delete=models.CASCADE, null=True, blank= True)
    year = models.PositiveIntegerField(null=True, blank= True)
    committed_amount = models.DecimalField(max_digits = 12, decimal_places= 2, null=True, blank= True)
    contributed_amount = models.DecimalField(max_digits = 12, decimal_places = 2, null=True, blank= True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('donor', 'year')
    def __str__(self):
        return f'{self.donor.donorName} {self.year}'
class School(models.Model):
    LEVEL=(
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Tertiary', 'Tertiary'),
    )
    LOCATION = (
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Kitale', 'Kitale'),
        ('Eldoret', 'Eldoret'),
        ('Nakuru', 'Nakuru'),
        ('Kajiado', 'Kajiado'),
        ('Laikipia', 'Laikipia'),
    )
    schoolName = models.CharField(max_length=100)
    schoolEmail = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)
    level = models.CharField(max_length=10, choices=LEVEL)
    location = models.CharField(max_length=20, choices=LOCATION)

    def __str__(self):
        return f'{self.schoolName}'

class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    LEVELofSUPPORT = (
        ('PrimaryOnly', 'PrimaryOnly'),
        ('Primary&Secondary', 'Primary&Secondary'),
        ('Primary&Secondary&Tertiary', 'Primary&Secondary&Tertiary'),
        ('Secondary&tertiary', 'Secondary&tertiary'),
        ('TertiaryOnly', 'TertiaryOnly'),
        ('SecondaryOnly', 'SecondaryOnly'),
        ('Primary&Tertiary', 'Primary&Tertiary'),
    )
    POSITION = (
        ('Continuing', 'Continuing'),
        ('Graduate', 'Graduate'),
        ('Undergraduate', 'Undergraduate'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    )
    STATUS = (
        ('Single-Orphan', 'Single-Orphan'),
        ('Double-Orphan', 'Double-Orphan'),
        ('Disadvantaged', 'Disadvantaged'),
        ('Disabled', 'Disabled'),
    )
    studentName = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=10, choices=GENDER, null=False)
    dateofbirth = models.DateField(null=False)
    intermediary = models.ForeignKey(Intermediary,related_name='intermediary', on_delete=models.CASCADE)
    donor = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    class_level = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=25, choices=POSITION, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
    level = models.CharField(max_length=100, choices=LEVELofSUPPORT, null=True, blank=True)
    backgroundInfo = models.TextField(null=True, blank=True)
    primary_school = models.ForeignKey(School, related_name='primary_students', on_delete=models.CASCADE, null=True, blank=True)
    secondary_school = models.ForeignKey(School, related_name='secondary_students', on_delete=models.CASCADE, null=True, blank=True)
    tertiary_school = models.ForeignKey(School, related_name='tertiary_students', on_delete=models.CASCADE, null=True, blank=True)
    profilePic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.studentName}'

class Employee(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    DEPARTMENT = (
        ('Research', 'Research'),
        ('Finance', 'Finance'),
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Data-entry', 'Data-entry'), 
    )
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE, null=True)
    employeeName = models.CharField(max_length=100)
    employeeEmail = models.EmailField(max_length=100, unique=True)
    employeePhone = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    department = models.CharField(max_length=10, choices=DEPARTMENT)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employeeName}'
    
class AcademicProgress(models.Model):
    YEAR = (
        ('2023','2023'),
        ('2024','2024'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, choices=YEAR)
    bursaries =models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.student.studentName}'
    
    def update_progress(self, year, class_level):
        if year == 2023:
            self.year = class_level
        if year == 2024:
            self.year = class_level
        self.save()

class Exam(models.Model):
    TERM_CHOICES = (
        ('Term1','Term1'),
        ('Term2','Term2'),
        ('Term3','Term3'),
    )
    exam_name= models.CharField(max_length=30)
    term = models.CharField(max_length=5, choices=TERM_CHOICES)
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.exam_name}'

class ExamResults(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f'{self.subject}, {self.score}'

    
