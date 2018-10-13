from django.urls import path
from django.conf.urls import url
from . import views
 
urlpatterns = [
    path('list/', views.home, name='home'),
    path('single-post/<post_id>/', views.single_post, name='single-post')
]