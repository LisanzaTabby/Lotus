from django.db import models
from django.contrib.auth.models import User

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
    level = models.CharField(max_length=10, choices=LEVEL)
    location = models.CharField(max_length=20, choices=LOCATION)

    def __str__(self):
        return f'{self.schoolName}'
class StudentPosition(models.Model):
    POSITION =(
        ('Continuing', 'Continuing'),
        ('Graduate', 'Graduate'),
        ('Undergraduate', 'Undergraduate'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    )
    position = models.CharField(max_length=25, choices=POSITION)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}'
class StudentPosition(models.Model):
    POSITION =(
        ('Continuing', 'Continuing'),
        ('Graduate', 'Graduate'),
        ('Undergraduate', 'Undergraduate'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    )
    position = models.CharField(max_length=25, choices=POSITION)
    def __str__(self):
        return f'{self.student}'
    
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
        ('Primary&Tertiary', 'Primany&Tertiary'),
    )
    studentName = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=10, choices=GENDER, null=False)
    dateofbirth = models.DateField(null=False)
    intermediary = models.ForeignKey(Intermediary, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, null=True, blank=True)
    class_level = models.CharField(max_length=20, null=True, blank=True)
    position = models.ForeignKey(StudentPosition, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, choices=LEVELofSUPPORT, null=True, blank=True)
    backgroundInfo = models.TextField(null=True, blank=True)
    primary_school = models.ForeignKey(School, related_name='primary_students', on_delete=models.CASCADE,null=True,blank=True)
    secondary_school = models.ForeignKey(School, related_name='secondary_students', on_delete=models.CASCADE,null=True,blank=True)
    tertiary_school = models.ForeignKey(School, related_name='tertiary_students', on_delete=models.CASCADE,null=True,blank=True)
    profilePic = models.ImageField(upload_to='profile_pics', blank=True, null=False)
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

class Status(models.Model):
    STATUS = (
        ('Single-Orphan', 'Single-Orphan'),
        ('Double-Orphan', 'Double-Orphan'),
        ('Disadvantaged', 'Disadvantaged'),
    )
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f'{self.status}'
    
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
    def updateprogress(self, year, class_level):
        if year == 2023:
            self.year = class_level
        elif year == 2024:
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
class ExamResults(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2,null=True, blank=True)

    def __str__(self):
        return f'{self.subject},{self.score}'
    
    

    


