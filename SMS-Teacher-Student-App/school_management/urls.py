"""school_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sms.urls')),
    path('', include('student.urls')),
    path('loginstudent/',views.loginstudent, name="loginstudent"),
    path('type/',views.acctype, name="accountstype_page"),
    path('student/',views.studentLogin, name="student_login"),
    path('teacher/',views.teach_Login, name="teacher_login"),
    path('parent/',views.parent_Login, name="parent_login"),
    path('admins/',views.admin_Login, name="admins_login"),
    path('addsubject/', views.addsubject, name="addsubject"),
    path('addmarks/', views.addmarks, name="addmarks"),
    path('addattend/', views.addattend, name="addattend"),
    path('addexams/', views.addexams, name="addexams"),
    path('attendance/', views.attendance, name="attendance"),
    path('marks/', views.marks, name="marks"),
    path('exams/', views.exams, name="exams"),
    path('subject/', views.subject, name="subject"),
    path('display_marks/', views.display_marks, name="display_marks"),
    path('display_attendance/', views.display_attendance, name="display_attendance"),
    path('display_timetable/', views.display_timetable, name="display_timetable"),
    path('changetable/', views.changetable, name="changetable"),
    path('timetable/', views.timetable, name="timetable"),
]

