from django.conf.urls import include, url
from . import views
<<<<<<< HEAD
from .views import search
=======
>>>>>>> b3618b8a125e1092767ae066f7ae983f48e8b0e0

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name= 'post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
<<<<<<< HEAD
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name= 'post_edit'),
    url(r'^post/search/$', views.search, name='search'),
=======
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name= 'post_edit')
>>>>>>> b3618b8a125e1092767ae066f7ae983f48e8b0e0
]
