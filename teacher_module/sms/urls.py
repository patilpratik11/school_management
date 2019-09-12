from django.urls import path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url
from . import templates
from . import views 

urlpatterns = [
	path('',views.index, name='index'),
    	path('teacher/login/addsubject', views.addsubject, name='addsubject'),
    	path('teacher/login', views.loginTeacher, name='login'),
#   	path('admin/login', views.loginAdmin, name='login'),
#   	path('parent/login', views.loginParent, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
