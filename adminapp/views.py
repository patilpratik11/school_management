from django.shortcuts import render
from .models import AdminModel
from student.models import StudentModell,ClassModell,ParentModell,STmapping
from sms.models import Teacher,Subject
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse
from django.template import RequestContext

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
    request_context = RequestContext(request)
    
    receiver = request.POST.get("toemail")




            

