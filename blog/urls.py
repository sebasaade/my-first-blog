from django.conf.urls import include, url
from . import views
from .views import search

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name= 'post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name= 'post_edit'),
    url(r'^post/search/$', views.search, name='search'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name= 'post_edit')
]
