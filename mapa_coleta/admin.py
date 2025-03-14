from django.contrib import admin
from .models import User , Teste_Api

class TesteApiAdmin(admin.ModelAdmin):
    list_display = ('numero_teste', 'nome', 'created_at')  # Campos que você deseja exibir no list

# Register your models here.
admin.site.register(User)
admin.site.register(Teste_Api, TesteApiAdmin)