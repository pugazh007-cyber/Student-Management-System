from django import forms
from .models import Student, Attendance, Mark
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student; fields='__all__'
        widgets={'dob':forms.DateInput(attrs={'type':'date'}),'address':forms.Textarea(attrs={'rows':3})}
class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance; fields='__all__'; widgets={'date':forms.DateInput(attrs={'type':'date'})}
class MarkForm(forms.ModelForm):
    class Meta:
        model=Mark; fields='__all__'
