
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 




urlpatterns = [
   
    path('parent/viewchild',views.viewchild,name="viewchild"),
    url('eanalysis',views.eanalysis, name="eanalysis"),
    url('marks',views.showmarks,name="showmarks"),
     



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)