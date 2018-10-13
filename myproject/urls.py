from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include('school.urls'), name='home'),
    path('info/', include('info.urls'), name='district'),
    path('student/',include('student.urls'), name='student'),
]
