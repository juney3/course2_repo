from django.shortcuts import render, redirect

from .models import Course, Course_Description, Course_Comment

# Create your views here.
def index(request):
	courses = Course.objects.all()
	descriptions = Course_Description.objects.all()
	comments = Course_Comment.objects.all()
	context = {
				'courses': courses, 
				'descriptions': descriptions, 
				'comments': comments
				}
	return render(request, 'index.html', context)

def add(request):
	course = Course.objects.create(name=request.POST['name'])
	description = Course_Description.objects.create(course=course, description=request.POST['description'])
	return redirect('/')

def remove(request, id):
	course = Course.objects.get(id=id)
	description = Course_Description.objects.get(course=course)
	context = {
				'course': course, 
				'description': description
				}
	return render(request, 'remove.html', context)

def delete(request, id):
	Course.objects.filter(id=id).delete()
	return redirect('/')

def comment(request, id):
	course = Course.objects.get(id=id)
	Course_Comment.objects.create(course=course, comment=request.POST['comment'])
	return redirect('/')
