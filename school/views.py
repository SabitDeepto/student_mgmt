from django.shortcuts import render
from .models import SchoolInfo

# Create your views here.
def home(request):
	all_post = SchoolInfo.objects.all()
	dyna = {'all_post_list':all_post}
	return render(request, 'school_list.html', dyna)

def single_post(request, post_id):
	post = SchoolInfo.objects.get(pk=post_id)
	return render(request, 'single_post.html', {'post':post})
