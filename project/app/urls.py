from django.conf.urls import url
from app import views

urlpatterns = [

	url('course-list', views.courses, name="courses"),


]