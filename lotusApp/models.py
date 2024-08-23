from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
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
    MODEOFSTUDY = (
        ('8-4-4', '8-4-4'),
        ('CBC', 'CBC'),
    )
    schoolName = models.CharField(max_length=100)
    location = models.CharField(max_length=10, choices=LOCATION)
    phone= models.CharField(max_length=10, unique=True)
    schoolEmail = models.EmailField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.schoolName}'
    
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
    location = models.CharField(max_length=10, choices=LOCATION)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.intermediaryName}'
    
class Donor(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
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
    studentName = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    intermediary = models.ForeignKey(Intermediary, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    backgroundInfo = models.TextField()
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
    employeeName = models.CharField(max_length=100)
    employeeEmail = models.EmailField(max_length=100, unique=True)
    employeePhone = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    department = models.CharField(max_length=10, choices=DEPARTMENT)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employeeName}'
    
class Results(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)



