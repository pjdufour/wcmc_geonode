from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^profile/password/$', 'django_ldapbackend.views.password_change'), (r'^profile/password/changed/$', 'django.contrib.auth.views.password_change_done'),
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
   url(r'^help/layers?$', TemplateView.as_view(template_name='help/layers.html'), name='helplayers'),
   url(r'^help/maps?$', TemplateView.as_view(template_name='help/maps.html'), name='helpmaps'),
   url(r'^help/documents?$', TemplateView.as_view(template_name='help/documents.html'), name='helpdocuments'),
   url(r'^help/people?$', TemplateView.as_view(template_name='help/people.html'), name='helppeople'),
   url(r'^help/groups?$', TemplateView.as_view(template_name='help/groups.html'), name='helpgroups'),
   url(r'^help/naming-standards?$', TemplateView.as_view(template_name='help/naming-standards.html'), name='helpnamingstandards'),
 ) + urlpatterns
