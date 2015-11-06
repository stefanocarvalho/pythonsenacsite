from django import forms

from django.contrib.auth.models import User

from .models import AnimalProfile

from .models import UserProfile

class UserForm(forms.ModelForm):
	#first_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'required'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user', 'data_cadastro')

class AnimalForm(forms.ModelForm):
	class Meta:
		model = AnimalProfile
		fields = ('sexo', 'idade', 'peso', 'preco',)