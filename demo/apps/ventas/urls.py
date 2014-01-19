from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.ventas.views',
	url(r'^add/producto/$','add_product_view',name="vista_agregar_producto"),
	url(r'^edit/producto/(?P<id_prod>.*)/$','edit_product_view',name="vista_editar_producto"),
	url(r'^add/festival/$','add_festival_view',name="vista_agregar_festival"),
	url(r'^edit/festival/(?P<id_fest>.*)/$','edit_festival_view',name="vista_editar_festival"),
	url(r'^add/video/$','add_video_view',name="vista_agregar_video"),
	url(r'^edit/video/(?P<id_vid>.*)/$','edit_video_view',name="vista_editar_video"),
)
