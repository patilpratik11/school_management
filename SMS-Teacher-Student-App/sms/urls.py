from django.urls import path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url
from . import templates
from . import views 

urlpatterns = [
	path('',views.index, name='index'),
    	path('teacher/loginteacher', views.loginTeacher, name='loginteacher'),
    	path('student/loginstudent', views.loginstudent, name='loginstudent'),
#   	path('admin/login', views.loginAdmin, name='loginadmin'),
#   	path('parent/login', views.loginParent, name='loginparent'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
