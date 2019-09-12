
from django.urls import path, include
from django.conf.urls import url
from student import views
from django.conf import settings
from django.conf.urls.static import static 
from .views import get_data


urlpatterns = [
    url('dashboard/',views.studentDashboard, name="student_dashboard"),
    url('eanalysis/',views.eanalysis, name="examana"),
    url('data/', get_data),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)