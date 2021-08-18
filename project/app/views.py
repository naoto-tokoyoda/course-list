from django.shortcuts import render
from app.models import Course
from django.core.paginator import Paginator


# Create your views here.
def courses(request):
    
	courses = Course.objects.order_by('course_code')
 
 	# #setup pagination
	# p = Paginator(course_list, 10)
	# page = request.GET.get('page')
	# courses = p.get_page(page)
	return render(request, 'app/index.html', {'courses': courses})


