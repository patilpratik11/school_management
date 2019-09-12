
from django.urls import path, include
from django.conf.urls import url
from student import views
from django.conf import settings
from django.conf.urls.static import static 
from .views import get_data,get_data1


urlpatterns = [
    url('dashboard/',views.studentDashboard, name="student_dashboard"),
    url('eanalysis/',views.eanalysis, name="examana"),
    url('aanalysis/',views.aanalysis, name="attana"),
    url('data/', get_data),
    url('data1/', get_data1),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)