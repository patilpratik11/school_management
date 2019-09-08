from django import forms
from student.models import Student_information


class Student_information_form(forms.ModelForm):
    class Meta:
        model = Student_information
        fields = {"first_name","middle_name","last_name"}

