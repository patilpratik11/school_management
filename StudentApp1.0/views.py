from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentModell, ClassModell, ParentModell, Student_attendence, Student_marks, ExamModell,SubjectModell, StudentParent
from django.db.models.functions import Cast
from django.db.models import IntegerField


# Create your views here.
loggedin_username = 'Johnny'
loggedin_id = 1

def studentDashboard(request):
    
    
    #joins student and class
    # func_value = StudentModell.objects.getfname()
    dbuser = StudentModell.objects.get(student_fname= loggedin_username)
    
    students = StudentModell.objects.select_related('class_id').all()

    # StudentParent.objects.get(id=dbuser.student_id).entry_set.Create(
    #     student_id = StudentModell.objects.get(student_id_id = dbuser.student_id),
    #     parent_id = ParentModell.objects.get(parent_fname = dbuser.mname)
    # )
    
    #Accessing Parent from DB
    #pid = StudentParent.objects.get(student_id_id=dbuser.student_id)
    #parents = ParentModell.objects.get(parent_id_id = pid.parent_id)

    

    attendence = Student_attendence.objects.filter(class_id_id = dbuser.class_id)

    return render(request, 'common/studentDashboard.html',{'students':students, 'attendence':attendence})

def eanalysis(request):
    dbuser = Student_marks.objects.filter(student_id_id= loggedin_id)
    return render(request,'common/eanalysis.html', {'dbuser':dbuser})

def aanalysis(request):
    return render(request,'common/aanalysis.html')        

sm = Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=1).values_list('marks', flat=True)
sm1 = Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=2).values_list('marks', flat=True)
sm2 = Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=3).values_list('marks', flat=True)
# temp =[]
# for i in sm: /
#     temp.append(sm[i])



def get_data(request):
    
	data = {
		'classtest_data': list(sm),
        'unittest_data': list(sm1),
        'finaltest_data': list(sm2),
		'label_data': ['History', 'Geography'],
	}

	return JsonResponse(data)

sa = Student_attendence.objects.filter(student_id_id= loggedin_id).values_list('attendence_percent', flat=True)



def get_data1(request):
    
	data1 = {
		'Attended_percent': list(sa),
		'label_data': ['History', 'Geography'],
	}

	return JsonResponse(data1)