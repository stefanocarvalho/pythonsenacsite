from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

class AnimalProfile(models.Model):
	SEXO_CHOICES = (
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    )
	id = models.AutoField(primary_key=True)
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
	idade = models.PositiveIntegerField()
	data_compra = models.DateTimeField(auto_now_add=True)
	peso = models.FloatField()
	preco = models.FloatField()


class Sobre(models.Model):
	titulo = models.CharField(u'Título da Página', max_length=50)
	descricao = models.TextField(u'Descrição')

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name='Sobre'
		verbose_name_plural='Sobre'