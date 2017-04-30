from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.posts_display, name = 'display'),
    url(r'^create/$', views.posts_create, name = 'create'),
    url(r'^update/$', views.posts_update, name = 'update'),
    url(r'^delete/$', views.posts_delete, name = 'delete'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name = 'detail'),
]
