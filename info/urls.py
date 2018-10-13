from django.urls import path
from django.conf.urls import url
from . import views
 
urlpatterns = [
    path('district/list', views.district, name='district'),
    # path('single-post/<post_id>/', views.single_post, name='single-post')
]