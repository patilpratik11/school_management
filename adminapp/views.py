from django.shortcuts import render
from .models import AdminModel
from student.models import StudentModell,ClassModell,ParentModell,STmapping
from sms.models import Teacher,Subject
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse,FileResponse
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from fusioncharts import FusionCharts
from collections import OrderedDict
import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape


# Create your views here.
def adminDashboard(request):
    dbuser = AdminModel.objects.get(student_fname= loggedin_username) 
    return render(request, 'common/studentDashboard.html',{'dbuser':dbuser})
@csrf_protect
def addStudent(request):
    request_context = RequestContext(request)
    try:
        student_fname = request.POST.get("first_name")
        student_mname = request.POST.get("middle_name")
        student_lname = request.POST.get("last_name")
        rollno = request.POST.get("rollno")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        class_id = request.POST.get("class")
        classobj = ClassModell.objects.get(class_id=class_id)
        blood_group = request.POST.get("bg")
        fee_status = request.POST.get("fee")
        parent_mname = request.POST.get("pmiddle_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        query = StudentModell(student_fname=student_fname,student_mname=student_mname,student_lname=student_lname,rollno=rollno,gender=gender,address=address,class_id=classobj,dob=dob,blood_group=blood_group,fee_status=fee_status)
        query.save()
        query1 = ParentModell(parent_fname = student_mname,parent_mname = parent_mname,parent_lname= student_lname,mobile=mobile,email= email,password=password)
        query1.save()
        sobj = StudentModell.objects.last()
        pobj = ParentModell.objects.last()
        query2 = STmapping(student_id = sobj,parent_id = pobj)
        query2.save()
        messages.info(request, 'Student Added Successfully')
        return render(request,'common/adminDashboard.html')
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/adminDashboard.html')

def addTeacher(request):
    request_context = RequestContext(request)
    try:
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        query = Teacher(first_name = first_name,middle_name=middle_name,last_name=last_name,email=email,password=password,mobile=mobile)
        query.save()
        messages.info(request,'Teacher Added Successfully')
        return render(request,'common/adminDashboard.html')
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/adminDashboard.html')

def removeStudent(request):
    request_context = RequestContext(request)
    try:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        class_name = request.POST.get("class")
        rollno = request.POST.get("rollno")
        class_id = ClassModell.objects.get(class_name=class_name)
        id = StudentModell.objects.filter(class_id=class_id).filter(rollno=rollno)
        id.delete()
        messages.info(request,'Student Deleted')
        return render(request,'common/adminDashboard.html')
    except Exception as e:
        messages.info(request.e)
        return render(request,'common/adminDashboard.html')

def removeTeacher(request):
    request_context = RequestContext(request)
    try:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        id = Teacher.objects.filter(email=email).filter(mobile=mobile)
        if id.delete():
            messages.info(request,'Teaher Remove')
            return render(request,'common/adminDashboard.html')
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/adminDashboard.html')

def addSubject(request):
    request_context = RequestContext(request)
    try:
        subject_name = request.POST.get("subject_name")
        query = Subject(subject_name=subject_name)
        query.save()
        messages.info(request,'Subject Added !')
        return render(request,'common/adminDashboard.html')
    except Exception as e:
        messages.info(request,e)
        return render(render,'common/adminDashboard.html')

def removeSubject(request):
    request_context = RequestContext(request)
    try:
        subject_name = request.POST.get("subject_name")
        id = Subject.objects.filter(subject_name=subject_name)
        if id.delete():
            messages.info(request,'Subject Deleted')
            return render(request,'common/adminDashboard.html')
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/adminDashboard.html')
   
def viewStudent(request):
    request_context = RequestContext(request)
    try:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        class_name = request.POST.get("class")
        rollno = request.POST.get("rollno")
        class_id = class_name
        s_obj = StudentModell.objects.get(rollno=rollno,class_id=class_id,student_fname=first_name) 
        pname = s_obj.getparentname()
        lname = s_obj.getlname()
        parentobj = ParentModell.objects.get(parent_fname=pname,parent_lname=lname)
        print(s_obj)
        print(parentobj)
        context = {'student':s_obj,'parent':parentobj}
        return render(request,'common/viewStudent.html',context)
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/adminDashboard.html')

def viewTeacher(request):
    return render(request,'common/viewTeacher.html')

def changePassword(request):
    return render(request,'common/adminDashboard.html')

def mailParent(request):
    # try:
    sub = request.POST.get("subject")
    to = request.POST.get('tomail')
    body = request.POST.get("body")
    student_id = request.POST.get("sid")
    parent_id = request.POST.get("pid")
    s = StudentModell.objects.get(student_id=student_id)
    p = ParentModell.objects.get(parent_id=parent_id)
    context={'student':s,'parent':p} 
        #email_from = settings.EMAIL_HOST_USER
    recipient_list = [to]
    print(sub)
    print(to)
    print(body)
    print(recipient_list)    
    send_mail(sub, body, 'admin@livehealth.in',recipient_list, fail_silently=False) 
    messages.info(request,'Mail Sent...!')   
    return render(request,'common/viewStudent.html',context)
    # except Exception as e:
    #     messages.info(request,e)
    #     return render(request,'common/adminDashboard.html')

def updateStudent(request):
    request_context = RequestContext(request)
    try:
        student_fname = request.POST.get("first_name")
        student_id=request.POST.get("sid")
        student_mname = request.POST.get("middle_name")
        student_lname = request.POST.get("last_name")
        rollno = request.POST.get("rollno")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        class_id = request.POST.get("class")
        classobj = ClassModell.objects.get(class_id=class_id)
        blood_group = request.POST.get("bg")
        fee_status = request.POST.get("fee")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        print(blood_group)
        s=StudentModell.objects.get(student_id=student_id)

        s.student_fname = student_fname 
        s.student_mname = student_mname
        s.student_lname = student_lname
        s.rollno = rollno
        s.dob = dob 
        s.class_id = classobj 
        s.blood_group = blood_group
        s.fee_status = fee_status
        s.save()
        #.upadate(student_fname=student_fname,student_mname=student_mname,student_lname=student_lname,rollno=rollno,gender=gender,class_id=classobj,dob=dob,blood_group=blood_group,fee_status=fee_status)
        p=ParentModell.objects.get(parent_fname=student_mname,email=email,mobile=mobile)
        #.upadate(parent_fname = student_mname,parent_lname= student_lname,mobile=mobile,email= email,password=password)
        context = {'student':s,'parent':p}
        messages.info(request,'Student Details Updated')
        return render(request,'common/viewStudent.html',context)
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/viewStudent.html')


def studentAnalysis(request):
    try:
        request_context = RequestContext(request)
        dataSource = OrderedDict()
        chartConfig = OrderedDict()
        chartConfig["caption"] = "Student Marks"
        chartConfig["subCaption"] = "Unit test Marks"
        chartConfig["xAxisName"] = "Subject"
        chartConfig["yAxisName"] = "Marks"
        chartConfig["numberSuffix"] = ""
        chartConfig["theme"] = "fusion"
        chartConfig["exportEnabled"]=1

        # The `chartData` dict contains key-value pairs of data
        chartData = OrderedDict()
        chartData["Math"] = 95
        chartData["Marathi"] = 80
        chartData["Hindi"] = 88
        chartData["English"] = 89
        chartData["Science"] = 91
        chartData["History"] = 75
        

        dataSource["chart"] = chartConfig
        dataSource["data"] = []

        
        for key, value in chartData.items():
            data = {}
            data["label"] = key
            data["value"] = value
            dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
        column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)

        return render(request, 'common/studentAnalysis.html', {'output': column2D.render()})
    except Exception as e:
        messages.info(request,e)
        return render(request,'common/studentAnalysis.html')
    
def resultGeneration(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def idGeneration(request):
    student_id = request.POST.get("sid")
    s=StudentModell.objects.get(student_id=student_id)
    cname=s.class_id.class_name
    
    #classobj = ClassModell.objects.get(class_id=class_id)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont('Helvetica', 24, leading = None)
    p.rect(100,300,400,450)
    p.drawString(115, 700, "S.V.K.Shah Vidya Mandir,Shahada")
    p.setFont('Helvetica', 20, leading = None)
    p.drawString(115, 650, "Name:")
    p.drawString(185, 650, s.student_fname+" "+s.student_mname+" "+s.student_lname)
    p.drawString(115, 600, "Roll No:")
    p.drawString(190, 600, str(s.rollno))
    p.drawString(115, 550, "Class:")
    p.drawString(185, 550, str(cname))
    p.drawString(115, 500, "DOB:")
    p.drawString(185, 500, str(s.dob))
    p.drawString(115, 450, "Address:")
    p.drawString(200, 450, s.address)
    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

    


 
    
    
    







            

