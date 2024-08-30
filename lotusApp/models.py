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
    position = models.CharField(max_length= 25, null=True, blank=True, default='Continuing')
    level = models.CharField(max_length=100, choices=LEVELofSUPPORT, null=True, blank=True) 
    backgroundInfo = models.TextField(null=True, blank=True)
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

class StudentPosition(models.Model):
    POSITION =(
        ('Continuing', 'Continuing'),
        ('Graduate', 'Graduate'),
        ('Undergraduate', 'Undergraduate'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    )
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    position = models.CharField(max_length=25, choices=POSITION)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}'


