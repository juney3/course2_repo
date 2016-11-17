from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Course_Description(models.Model):
	description = models.TextField(max_length=500)
	course = models.OneToOneField('Course', on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Course_Comment(models.Model):
	comment = models.CharField(max_length=255)
	course = models.ForeignKey('Course', on_delete=models.CASCADE,)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

