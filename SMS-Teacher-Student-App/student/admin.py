from django.contrib import admin
from .models import StudentModell, ClassModell, ParentModell, Student_attendence, Student_marks, SubjectModell, ExamModell, STmapping



# Register your models here.
admin.site.register(StudentModell)
admin.site.register(ClassModell)
admin.site.register(ParentModell)
admin.site.register(Student_attendence)
admin.site.register(Student_marks)
admin.site.register(SubjectModell)
admin.site.register(ExamModell)
#admin.site.register(StudentParent)
admin.site.register(STmapping)
