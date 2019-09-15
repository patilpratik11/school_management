from django.shortcuts import render
from django.http import JsonResponse
from student.models import StudentModell, ClassModell, ParentModell, Student_attendence, Student_marks, ExamModell,SubjectModell, StudentParent, STmapping
from django.db.models.functions import Cast
from sms.models import Attendance,Teacher,ClassTeacher
from django.db.models import IntegerField
from student import views
from django.contrib import messages

# Create your views here.


def viewchild(request):
    try:
        student_id=request.POST.get("student")
        print(student_id)
    
        students = StudentModell.objects.get(student_id=student_id)
        print("*******======**")
        print(students)
        """att=Student_attendence.objects.get(student_id =student_id)
        print(att.getattend)
        class_name=students.getclassname.getclassname
    
        class_tech=ClassTeacher.objects.get(class_name = class_name)
    

        teacher_id=class_tech.getTeacher_id()

        teacher=Teacher.object.get(teacher_id = teacher_id)

        print(teacher)"""
      
        return render(request,'common/viewchild.html',{'students':students})
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/viewchild.html')




