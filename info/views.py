from django.shortcuts import render
from .models import District

# Create your views here.
def district(request):
	all_post = District.objects.filter()
	dyna = {'all_post_list':all_post}
	return render(request, 'district.html', dyna)
