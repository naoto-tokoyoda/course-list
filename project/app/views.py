from django.shortcuts import render
from app.models import Course
from django.core.paginator import Paginator


# Create your views here.
def courses(request):
	courses = Course.objects.order_by('course_code')
 
	return render(request, 'app/index.html', {'courses': courses})


