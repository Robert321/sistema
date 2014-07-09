from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from sistema.apps.registro.views import *
urlpatterns = patterns('sistema.apps.registro.views',
    # Examples:
    # url(r'^$', 'sistema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   	url(r'^$','index_view',name='vista_principal'),
    url(r'^carrera/$','addCarrera',name='vista_carrera'),
    #url(r'^contacto/$','contacto_view',name='vista_contacto'),
    url(r'^vercontacto/$','VerContacto',name='ver_contacto'),
    url(r'^agregarestudiante/','addEstudiante',name='vista_estudiante'),
    url(r'^menuestudiante/(?P<id>\d+)/$','MenuEstudiante',name='vista_menuestudiante'),
    url(r'^menudocente/(?P<id>\d+)/$','MenuDocente',name='vista_menudocente'),
    url(r'^agregardocente/','addDocente',name='vista_docente'),
    #url(r'^login/$','login_view_Estudiante',name='vista_login'),
    #url(r'^logout/$','logout_view_Estudiante',name='vista_logout'),
    url(r'^editarestudiante/(?P<id>\d+)/$',editar_estudiante),
    url(r'^editardocente/(?P<id>\d+)/$',editar_docente),
    url(r'^agregarmateria/',addMateria),
    url(r'^programar/',addRelEstMat),
    url(r'^agregarnotas/',addNotas),
    url(r'^registro/exito/$',exito),
)
