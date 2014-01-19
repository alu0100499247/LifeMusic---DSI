from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import grupo
from demo.apps.ventas.forms import addFestivalForm
from demo.apps.ventas.models import festivals
from demo.apps.ventas.forms import addVideoForm
from demo.apps.ventas.models import videos
from django.http import HttpResponseRedirect


def edit_product_view(request,id_prod):
	info = "Inicializando"
	prod = grupo.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			form.save_m2m()
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Modificado satisfactoriamente"
			return HttpResponseRedirect('/grupo/%s'%edit_prod.id)
	else:
		form = addProductForm(instance=prod)
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/editProducto.html',ctx,context_instance=RequestContext(request))


def add_product_view(request):
	info = "Inicializando"
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la info
			form.save_m2m() # Guarda las relaciones ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/grupo/%s'%add.id)
	else:
		form = addProductForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request)) 


def edit_festival_view(request,id_fest):
	info = "Inicializando"
	fest = festivals.objects.get(pk=id_fest)
	if request.method == "POST":
		form = addFestivalForm(request.POST,request.FILES,instance=fest)
		if form.is_valid():
			edit_fest = form.save(commit=False)
			form.save_m2m()
			edit_fest.status = True
			edit_fest.save() # Guardamos el objeto
			info = "Modificado satisfactoriamente"
			return HttpResponseRedirect('/festival/%s'%edit_fest.id)
	else:
		form = addFestivalForm(instance=fest)
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/editFestival.html',ctx,context_instance=RequestContext(request))


def add_festival_view(request):
	info = "Inicializando"
	if request.method == "POST":
		form = addFestivalForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la info
			form.save_m2m() # Guarda las relaciones ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/festival/%s'%add.id)
	else:
		form = addFestivalForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/addFestival.html',ctx,context_instance=RequestContext(request)) 


def edit_video_view(request,id_vid):
	info = "Inicializando"
	vid = videos.objects.get(pk=id_vid)
	if request.method == "POST":
		form = addVideoForm(request.POST,request.FILES,instance=vid)
		if form.is_valid():
			edit_vid = form.save(commit=False)
			form.save_m2m()
			edit_vid.status = True
			edit_vid.save() # Guardamos el objeto
			info = "Modificado satisfactoriamente"
			return HttpResponseRedirect('/video/%s'%edit_vid.id)
	else:
		form = addVideoForm(instance=vid)
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/editVideo.html',ctx,context_instance=RequestContext(request))


def add_video_view(request):
	info = "Inicializando"
	if request.method == "POST":
		form = addVideoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save() # Guardamos la info
			form.save_m2m() # Guarda las relaciones ManyToMany
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/video/%s'%add.id)
	else:
		form = addVideoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('ventas/addVideo.html',ctx,context_instance=RequestContext(request)) 


