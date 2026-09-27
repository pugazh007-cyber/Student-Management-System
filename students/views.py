from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Attendance, Mark
from .forms import StudentForm, AttendanceForm, MarkForm


def dashboard(request):
    return render(request, 'dashboard.html', {
        'total_students': Student.objects.count(),
        'total_attendance': Attendance.objects.count(),
        'total_marks': Mark.objects.count(),
    })


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'edit_student.html', {'form': form, 'student': student})


def delete_student(request, id):
    get_object_or_404(Student, id=id).delete()
    return redirect('student_list')


def attendance(request):
    form = AttendanceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('attendance')
    return render(request, 'attendance.html', {
        'form': form,
        'records': Attendance.objects.select_related('student').all().order_by('-date'),
    })


def marks(request):
    form = MarkForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('marks')
    return render(request, 'marks.html', {
        'form': form,
        'records': Mark.objects.select_related('student').all(),
    })
