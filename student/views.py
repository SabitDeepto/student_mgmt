from django.shortcuts import render
from .models import Guardian, Student


# Create your views here.

def guardian_list(request):
	all_post = Guardian.objects.all()
	context = {'all_post_list':all_post}
	return render(request, 'guardian_list.html', context)

def single_post(request, post_id):
	post = Guardian.objects.get(pk=post_id)
	return render(request, 'guardian_detail.html', {'post':post})

def student_list(request):
	all_post = Student.objects.all()
	context = {'all_post_list':all_post}
	return render(request, 'student_list.html', context)

def student_detail(request, post_id):
	post = Student.objects.get(pk=post_id)
	return render(request, 'student_detail.html', {'post':post})