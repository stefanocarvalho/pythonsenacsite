from django.conf.urls import url

from boi.core.views import *
urlpatterns = [
	url(r'^$', index, name='index'),
    url(r'^cadastro-animal/$', cadastro_animal, name='cadastroanimal'),
    url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    url(r'^login/$', user_login, name='userlogin'),
    url(r'^logout/$', user_logout, name='userlogout'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
    url(r'^sucesso-animal/$', sucesso_animal, name='animalsucesso'),
    url(r'^tela-usuario/$', tela_usuario, name='telausuario'),
    url(r'^editar-animal/(?P<id>\d+)/$', editar_animal, name='editaranimal'),
    url(r'^deletar-animal/(?P<id>\d+)/$', apagar_animal, name='apagaranimal'),
    url(r'^lista-animal/$', lista_animais, name='listaanimais'),
    url(r'^sobre/$', sobre, name='sobre'),
    url(r'^index/$', index, name='index'),
    


]
