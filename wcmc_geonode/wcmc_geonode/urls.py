from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
   url(r'^help/layers?$', TemplateView.as_view(template_name='help/layers.html'), name='helplayers'),
 ) + urlpatterns
