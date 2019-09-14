from django.urls import path, include
from django.conf.urls import url
from adminapp import views
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    url('dashboard/',views.adminDashboard, name="admin_dashboard"),
    url('addstudent',views.addStudent, name="addstudent"),
    url('addteacher',views.addTeacher, name="addteacher"),
    url('removestudent',views.removeStudent, name="removestudent"),
    url('removeteacher',views.removeTeacher, name="removeteacher"),
    url('addsubject',views.addSubject, name="addsubject"),
    url('removesubject',views.removeSubject, name="removesubject"),
    url('viewstudent',views.viewStudent, name="viewstudent"),
    url('viewteacher',views.viewTeacher, name="viewteacher"),
    url('changepassword',views.changePassword, name="changepassword"),
    url('mailparent',views.mailParent, name="mailparent"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)