# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_display(request):
	posts = Post.objects.all()
	context = {
		'title': 'Posts',
		'posts': posts,
	}
	return render(request, 'index.html', context)

def posts_create(request):
	return HttpResponse("<h1>Create!</h1>")

def posts_delete(request):
	return HttpResponse("<h1>Delete!</h1>")

def posts_update(request):
	return HttpResponse("<h1>Update!</h1>")

def post_detail(request):
	context = {
		'title': 'Post Detail',
	}
	return render(request, 'post_detail.html', context)