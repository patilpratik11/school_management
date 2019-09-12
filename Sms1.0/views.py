from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'common/index.html') 

def acctype(request):
    return render(request, 'common/accounts.html')    

def studentLogin(request):
    return render(request, 'common/login_student.html')    

def teach_Login(request):
    id = 1
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })

def parent_Login(request):
    id = 2
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })

def admin_Login(request):
    id = 3
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })    