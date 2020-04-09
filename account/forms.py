from django import forms
from .models import Student,Teacher

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['institute','image',"interests"]
        

class Teacher_form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['institute','image',"qualifications","status"]
        