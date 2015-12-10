from django.conf.urls import patterns, include, url
from django.contrib import admin
from aplicacion.views import *
import aplicacion.views as views

admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),    
    url(r'^$','aplicacion.views.index', name='index'),
    url(r'^registrar/$', Registrar.as_view(), name='registrar'),
    url(r'^registrado/$', Registrado.as_view(), name='registrado'),
    url(r'^consultar/$', Consultar.as_view(), name='consultar'),
)