from django.conf.urls import url
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', views.posts_page, name = 'posts'),
]
