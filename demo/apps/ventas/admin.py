from django.contrib	import admin
from demo.apps.ventas.models import cliente,grupo,categoriaProducto,festivals,videos

class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre','thumbnail','titulo','link')
	list_filter = ('autor','link')
	search_fields = ['nombre','autor','titulo']
	fields = ('nombre','autor','titulo','descripcion','link','stock','imagen','categorias','status')




admin.site.register(cliente)
admin.site.register(grupo,productoAdmin)
admin.site.register(categoriaProducto)
admin.site.register(festivals)
admin.site.register(videos)
