from django.conf.urls import url, include
from django.contrib import admin
from posts import views

urlpatterns = [
	# url(r'^$', include('landing_page.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls', namespace = 'posts')),
]
