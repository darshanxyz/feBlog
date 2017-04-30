# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'updated', 'posted']
	list_display_links = ['updated']
	list_editable = ['title']
	list_filter = ['updated', 'posted']
	search_fields = ['title', 'content']
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
