# Create your views here.
from django.http import HttpResponse
from demo.apps.ventas.models import grupo
from demo.apps.ventas.models import videos
from demo.apps.ventas.models import festivals
# Integramos la serializacion de los objetos
from django.core import serializers


def wsProductos_view(request):
	data = serializers.serialize("json",grupo.objects.filter(status=True))
	# Devuelve la informacion en formato json
	return HttpResponse(data,mimetype='application/json')

def wsVideos_view(request):
	data = serializers.serialize("json",videos.objects.filter(status=True))
	# Devuelve la informacion en formato json
	return HttpResponse(data,mimetype='application/json')

def wsFestivales_view(request):
	data = serializers.serialize("json",festivals.objects.filter(status=True))
	# Devuelve la informacion en formato json
	return HttpResponse(data,mimetype='application/json')

