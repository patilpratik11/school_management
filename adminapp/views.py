from django.shortcuts import render
from .models import AdminModel
from student.models import StudentModell,ClassModell
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
        gender = request.POST.get("M")
        class_id = request.POST.get("class")
        classobj = ClassModell.objects.get(class_id=class_id)
        blood_group = request.POST.get("bg")
        fee_status = request.POST.get("fee")
        query = StudentModell(student_fname=student_fname,student_mname=student_mname,student_lname=student_lname,rollno=rollno,gender=gender,address=address,class_id=classobj,dob=dob,blood_group=blood_group,fee_status=fee_status)
        query.save()
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



            

