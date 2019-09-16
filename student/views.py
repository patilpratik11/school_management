from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.db.models.functions import Cast
from django.db.models import IntegerField
from sms.models import *
from adminapp.models import holidaylist
import datetime
from datetime import datetime, date


# Logged In user details accessed.
lotable = LoginS.objects.first()
loggedin_id = lotable.getId()
#loggedin_user = LoginS.objects.get().first()


def studentDashboard(request):
    
    
    #joins student and class
    dbuser = StudentModell.objects.get(student_id= loggedin_id)
    
    students = StudentModell.objects.select_related('class_id').all()
    
    attendence = Student_attendence.objects.filter(class_id_id = dbuser.class_id)
    classinfo = dbuser.class_id

    temp = dbuser.student_id
    stmappingobject = STmapping.objects.get(student_id=temp)
    parentobject = stmappingobject.parent_id
    



    
    return render(request, 'common/studentDashboard.html',{'dbuser':dbuser, 'attendence':attendence,'classinfo':classinfo, 'parentobject':parentobject, 'holidays':holidays})

def eanalysis(request):
    dbuser = Student_marks.objects.filter(student_id_id= loggedin_id)
    return render(request,'common/eanalysis.html', {'dbuser':dbuser})

def showtt(request):
    table = Timetable.objects.all()
    return render(request,'common/disptt.html',{'table':table})

def showmarks(request):
    
    loginobj = Login.objects.all().first()

    try:

        
        classtestmarks = []
        unittestmarks= []
        finaltestmakrs = []
        classtestmarks = Marks.objects.filter(student_id_id= loggedin_id).filter(exam_types_id='Class Test')
        unittestmarks = Marks.objects.filter(student_id_id= loggedin_id).filter(exam_types_id='Unit Test')
        finaltestmarks = Marks.objects.filter(student_id_id= loggedin_id).filter(exam_types_id='Final Test')
        subjids = Marks.objects.filter(student_id_id= loggedin_id).values_list('subject_name',flat=True).distinct()
        subjs = []
        count = 0
        for x in subjids:
            e = Subject.objects.get(subject_id=subjids[count])
            q = e.subject_name
            subjs.append(e)
            count = count + 1 
        return render(request, 'common/dispmarks.html', {'classtestmarks':classtestmarks, 'unittestmarks':unittestmarks,'finalexammarks':finaltestmarks, 'subjs':subjs})    

    except:		
        return render(request, 'common/dispmarks.html')		 		
		
def showatt(request):
    absentdates = Attendance.objects.filter(student_id_id=loggedin_id).values_list('date', flat=True)
    return render(request,'common/checkatt.html',{'absentdates':absentdates})



def get_data(request):
	data = {
		'classtest_data': list(Marks.objects.filter(student_id_id= loggedin_id).filter(exam_types_id='Class Test').values_list('marks', flat=True)),
        'unittest_data': list(Marks.objects.filter(student_id_id= loggedin_id).filter(exam_types_id='Unit Test').values_list('marks', flat=True)),
        'finaltest_data': list(Marks.objects.filter(student_id_id= loggedin_id).filter(exam_types_id='Final Test').values_list('marks', flat=True)),
		'label_data': ['History', 'Geography','Maths','Science','English','Marathi'],
	}

	return JsonResponse(data)

def showholidays(request):
    holidays = holidaylist.objects.all().order_by('-datez')
    temp = []
    for x in holidays:
        dateobj = x.datez
        cur_dateobj = date.today()
        diffs = dateobj - cur_dateobj
        if diffs.days <= 3:
            if diffs.days >= 1:
                temp.append(x)
    
    return render(request, 'common/showholiday.html', {'holidays':temp})
    return render(request, 'common/showholiday.html')    






