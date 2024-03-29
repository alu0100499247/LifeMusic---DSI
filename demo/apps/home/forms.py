from django import forms

class ContactForm(forms.Form):
	Email	= forms.EmailField(widget=forms.TextInput())
	Titulo	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
	Email 				= forms.EmailField(widget=forms.TextInput())
	Username 			= forms.CharField(widget=forms.TextInput())
	Password 			= forms.CharField(widget=forms.PasswordInput(render_value=False))
	Repetir_Password 	= forms.CharField(widget=forms.PasswordInput(render_value=False))
	Vivo				= forms.CharField(widget=forms.TextInput())
	Genero				= forms.CharField(widget=forms.Textarea())