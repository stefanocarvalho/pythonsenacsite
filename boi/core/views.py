from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import AnimalForm, UserForm, UserProfileForm
from .models import Sobre,  AnimalProfile



def home(request):
	return render(request, 'base.html')	    
	    
def cadastro_animal(request):
	if not request.user.is_authenticated():
		return redirect('core:userlogin')
	if request.method == 'POST':
		animal_form = AnimalForm(request.POST, request.FILES)
		if animal_form.is_valid():
			animal_form.save()
			return redirect('core:animalsucesso')
		else:
			print(animal_form.errors)
	else:
		animal_form = AnimalForm()
	return render(request, 'core/cadastro_animal.html', {'animal_form': animal_form})

def sucesso_animal(request):
	return render(request, 'core/sucesso_animal.html')

def cadastro_usuario(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'foto' in request.FILES:
				profile.foto = request.FILES['foto']

			profile.save()
			return redirect('core:usuariosucesso')
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'core/cadastro_usuario.html',\
		{'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('core:listaanimais')
			else:
				return HttpResponse("Sua conta esta desativada.")
		else:
			return render(request, 'core/erro_login.html')
	return render(request, 'core/form_login.html')

def user_logout(request):
	logout(request)
	return redirect('core:index')

def sucesso_usuario(request):
	return render(request, 'core/sucesso_usuario.html')

def tela_usuario(request):
	return render(request, 'core/tela_user.html')

def sobre(request):
	sobre = Sobre.objects.all()
	return render(request, 'core/sobre.html', {'sobre':sobre})

def lista_animais(request):
	if not request.user.is_authenticated():
		return redirect('core:userlogin')
	animais = AnimalProfile.objects.all()
	return render(request, 'core/lista_animais.html', {'animais': animais})

def apagar_animal(request, id):
	animal = AnimalProfile.objects.get(id=id).delete()
	return redirect('core:listaanimais')

def editar_animal(request, id):
	animal = AnimalProfile.objects.get(id=id)
	if request.method == 'POST':
		animal_form = AnimalForm(request.POST, instance=animal)
		if animal_form.is_valid():
			animal_form.save()
			return redirect('core:listaanimais')
		else:
			print(animal_form.errors)

	else:
		animal_form = AnimalForm(instance=animal)
	return render(request, 'core/editar_animal.html', {'animal_form': animal_form})
	return redirect('core:listaanimais')

def index(request):
	animais = AnimalProfile.objects.all()
	femeas = AnimalProfile.objects.filter(sexo='F')
	machos = AnimalProfile.objects.filter(sexo='M')
	return render(request, 'core/index.html', {'animais': animais, 'femeas': femeas, 'machos' : machos})