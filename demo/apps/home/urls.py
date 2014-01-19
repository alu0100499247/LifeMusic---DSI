from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('demo.apps.home.views',
 	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^grupos/page/(?P<pagina>.*)/$','grupos_view',name='vista_grupos'),
	url(r'^grupo/(?P<id_prod>.*)/$','singleProduct_view',name='vista_single_producto'),
	url(r'^festival/page/(?P<pagina>.*)/$','festival_view',name='vista_festival'),
	url(r'^festival/(?P<id_fest>.*)/$','singleFestival_view',name='vista_single_festival'),
	url(r'^video/page/(?P<pagina>.*)/$','videos_view',name='vista_video'),
	url(r'^video/(?P<id_vid>.*)/$','singleVideo_view',name='vista_single_video'),
	url(r'^contacto/$', 'contacto_view',name='vista_contacto'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	url(r'^registro/$','registro_view',name='vista_registro'),
)
