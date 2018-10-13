from django.urls import path
from django.conf.urls import url
from . import views
 
urlpatterns = [
    path('guardian/', views.guardian_list, name='student'),
    path('guardian/<int:post_id>/', views.single_post, name='single-post'),

    path('list/', views.student_list, name='list'),
    path('detail/<post_id>/', views.student_detail, name='student_detail'),
]