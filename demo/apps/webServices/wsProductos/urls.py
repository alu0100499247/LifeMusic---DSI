from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.webServices.wsProductos.views',
	url(r'^ws/productos/$','wsProductos_view',name="ws_productos_url"),
	url(r'^ws/videos/$','wsVideos_view',name="ws_videos_url"),
	url(r'^ws/festival/$','wsFestivales_view',name="ws_festival_url"),
)


