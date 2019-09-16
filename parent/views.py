from django.shortcuts import render
from django.http import JsonResponse
from student.models import StudentModell, ClassModell, ParentModell, Student_attendence, Student_marks, ExamModell,SubjectModell, StudentParent, STmapping
from django.db.models.functions import Cast
from sms.models import Attendance,Teacher,ClassTeacher,Timetable,Marks,Subject
from adminapp.models import holidaylist
from django.db.models import IntegerField
from student import views
from django.contrib import messages
import datetime
from datetime import datetime, date
from fusioncharts import FusionCharts
from collections import OrderedDict
from django.http import HttpResponse



# Create your views here.


def viewchild(request):

        student_id=request.POST.get("student")
        students = StudentModell.objects.get(student_id=student_id)
        student_roll=students.getrollno()
        class_obj=students.getclassname()
        class_name=class_obj.getclassname()
        class_tech_obj=ClassTeacher.objects.get(class_name = class_name)
        teacher_id=class_tech_obj.getTeacher_id()
        print(teacher_id)
        id = Teacher.objects.get(teacher_id=teacher_id)
        
        attendanceobj =list( Attendance.objects.filter(student_roll = student_roll,class_name=class_name))
        tableobj = Timetable.objects.all()
       
        holidays = holidaylist.objects.all().order_by('-datez')
        print(holidays)
        temp = []
        for x in holidays:
            dateobj = x.datez
            cur_dateobj = date.today()
            diffs = dateobj - cur_dateobj
            print(diffs)
            if diffs.days <= 5:
                if diffs.days >= 1:
                    temp.append(x)

        print(temp)
        return render(request,'common/viewchild.html',{'students':students,'teacher':id,'dbuser':attendanceobj,'table':tableobj,'holidays':temp})

"""def eanalysis(request):
    
    student_id=request.POST.get("student")
    students = StudentModell.objects.get(student_id=student_id)
    print(students)
    
    return render(request,'common/eanalysisparent.html', {'dbuser':students})


def get_data(request):
	data = {
		'classtest_data': list( Marks.objects.filter(student_id_id= student_id).filter(exam_type='Class Test')),
        'unittest_data': list(Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=2).values_list('marks', flat=True)),
        'finaltest_data': list(Student_marks.objects.filter(student_id_id= loggedin_id).filter(exam_type_id=3).values_list('marks', flat=True)),
		'label_data': ['History', 'Geography','Maths','Science','English','Marathi'],
	}

	return JsonResponse(data)
    
"""
			
	
def showmarks(request):
   
    student_id=request.POST.get("student")
    print(student_id)
    try:

        classtestmarks = []
        unittestmarks= []
        finaltestmakrs = []
        classtestmarks = Marks.objects.filter(student_id_id= student_id).filter(exam_type='Class Test')
        unittestmarks = Marks.objects.filter(student_id_id= student_id).filter(exam_type='Unit Test')
        finaltestmarks = Marks.objects.filter(student_id_id= student_id).filter(exam_type='Final Test')
        subjids = Marks.objects.filter(student_id_id=student_id).values_list('subject_name',flat=True).distinct()
        print(classtestmarks )
        print(unittestmarks)
        print(finaltestmarks)
        print(subjids)
        subjs = []
        count = 0
        for x in subjids:
            e = Subject.objects.get(subject_id=subjids[count])
            print(e)
            q = e.subject_name
            subjs.append(e)
            count = count + 1
        return render(request, 'common/displaymarks.html', {'classtestmarks':classtestmarks, 'unittestmarks':unittestmarks,'finaltestmarks':finaltestmarks, 'subjs':subjs})  

    except:		
        return render(request, 'common/displaymarks.html')	


def eanalysis(request):

    student_id=request.POST.get("student")
    print(student_id)
    classtestmarks = []
    unittestmarks= []
    finaltestmakrs = []
    classtestmarks = Marks.objects.filter(student_id_id= student_id).filter(exam_type='Class Test')
    unittestmarks = Marks.objects.filter(student_id_id= student_id).filter(exam_type='Unit Test')
    finaltestmarks = Marks.objects.filter(student_id_id= student_id).filter(exam_type='Final Test')
    print(classtestmarks )
    marks=[]
    sub=[]
    subjs=[]
    count=0
    for obj in classtestmarks:
        m=obj.getMarks()
        marks.append(m)
        q=obj.getSubject()
        e = Subject.objects.get(subject_id=q)
        print(e)
        subjs.append(e)
        s=e.subject_name
        sub.append(s)
        count=count+1
        
    #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Class Test Result"
    chartConfig["subCaption"] = ""
    chartConfig["xAxisName"] = "Subject"
    chartConfig["yAxisName"] = "Marks"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs of data
    chartData = OrderedDict()
    for i in range(0,len(marks)):
        chartData[sub[i]] = marks[i]
    

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)



    

    return render(request, 'common/resultchart.html',{'output':column.render(),'classtestmarks':classtestmarks,'subjs':subjs})