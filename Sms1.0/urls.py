from django.urls import path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url

from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('type/',views.acctype, name="accountstype_page"),
    path('student/',views.studentLogin, name="student_login"),
    path('teacher/',views.teach_Login, name="teacher_login"),
    path('parent/',views.parent_Login, name="parent_login"),
    path('admins/',views.admin_Login, name="admins_login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)