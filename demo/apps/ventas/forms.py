from django import forms
from demo.apps.ventas.models import grupo
from demo.apps.ventas.models import festivals
from demo.apps.ventas.models import videos

class addProductForm(forms.ModelForm):
	class Meta:
		model 	= grupo
		exclude	= {'status',}

class addFestivalForm(forms.ModelForm):
	class Meta:
		model 	= festivals
		exclude	= {'status',}

class addVideoForm(forms.ModelForm):
	class Meta:
		model 	= videos
		exclude	= {'status',}

