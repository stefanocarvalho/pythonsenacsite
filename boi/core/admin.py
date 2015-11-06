from django.contrib import admin

from .models import AnimalProfile, UserProfile, Sobre

class UserProfileAdmin(admin.ModelAdmin):
	pass

class AnimalProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'sexo', 'data_compra', 'preco')
	search_fields = ('id', 'preco')


class SobreAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AnimalProfile, AnimalProfileAdmin)
admin.site.register(Sobre, SobreAdmin)