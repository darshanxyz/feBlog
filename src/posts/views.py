# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def posts_page(request):
	return HttpResponse("<h1>Hello!</h1>")