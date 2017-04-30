# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post
from .forms import PostForm

def posts_display(request):
	posts = Post.objects.all()
	context = {
		'title': 'Posts',
		'posts': posts,
	}
	return render(request, 'post_display.html', context)

def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form_instance = form.save(commit = False)
		form_instance.save()
		return HttpResponseRedirect(form_instance.get_absolute_url())

	context = {
		'form': form
	}
	return render(request, 'create_post.html', context)

def posts_delete(request, id):
	post = get_object_or_404(Post, id = id)
	post.delete()
	return redirect('posts:display')

def posts_update(request, id):
	post = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, instance = post)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'post': post,
		'title': post.title,
		'form': form,
	}
	return render(request, 'update_post.html', context)

def post_detail(request, id):
	post = get_object_or_404(Post, id = id)
	context = {
		'post': post,
		'title': post.title,
	}
	return render(request, 'post_detail.html', context)