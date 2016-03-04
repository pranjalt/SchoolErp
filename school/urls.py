from django.conf.urls import patterns, url
from school import views

urlpatterns = patterns('',
  url(r'^schoolList/', views.school_list, name='school_list'),
#  url(r'^new$', views.school_create, name='school_create'),
# url(r'^edit/(?P<pk>\d+)$', views.school_update, name='school_edit'),
# url(r'^delete/(?P<pk>\d+)$', views.school_delete, name='school_delete'),
)