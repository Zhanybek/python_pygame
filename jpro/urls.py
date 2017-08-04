from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^jonny/', views.jonny, name='jonny'),
    url(r'^get_scipt/', views.controller, name='controller'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

'''
urlpatterns = patterns('',
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>\d{4})/$', views.year_archive),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.article_detail),
)
'''