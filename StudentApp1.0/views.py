from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentModell, ClassModell, ParentModell, Student_attendence, Student_marks, ExamModell,SubjectModell, StudentParent, STmapping
from django.db.models.functions import Cast
from django.db.models import IntegerField


# Logged In user details accessed.
loggedin_username = 'Johnny'
loggedin_id = 1

def studentDashboard(request):
    
    
    #joins student and class
    dbuser = StudentModell.objects.get(student_fname= loggedin_username)
    
    students = StudentModell.objects.select_related('class_id').all()
    
    attendence = Student_attendence.objects.filter(class_id_id = dbuser.class_id)
    classinfo = dbuser.class_id

    temp = dbuser.student_id
    stmappingobject = STmapping.objects.get(student_id=temp)
    parentobject = stmappingobject.parent_id
    
    return render(request, 'common/studentDashboard.html',{'dbuser':dbuser, 'attendence':attendence,'classinfo':classinfo, 'parentobject':parentobject})

def eanalysis(request):
    dbuser = Student_marks.objects.filter(student_id_id= loggedin_id)
    return render(request,'common/eanalysis.html', {'dbuser':dbuser})


def get_data(request):
	data = {
		'classtest_data': list(Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=1).values_list('marks', flat=True)),
        'unittest_data': list(Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=2).values_list('marks', flat=True)),
        'finaltest_data': list(Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=3).values_list('marks', flat=True)),
		'label_data': ['History', 'Geography','Maths','Science','English','Marathi'],
	}

	return JsonResponse(data)



