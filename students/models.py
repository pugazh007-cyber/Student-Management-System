from django.db import models

class Student(models.Model):
    register_no=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    year=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    dob=models.DateField()
    address=models.TextField()
    def __str__(self): return f'{self.register_no} - {self.name}'

class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=10,choices=[('Present','Present'),('Absent','Absent')])
    def __str__(self): return f'{self.student.name} - {self.date} - {self.status}'

class Mark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    mark=models.IntegerField()
    def __str__(self): return f'{self.student.name} - {self.subject} - {self.mark}'
