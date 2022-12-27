from django.contrib import admin

from .models import Cad_Funcionario, Cad_Cliente

class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'email')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'email')    

admin.site.register(Cad_Funcionario, FuncionariosAdmin)
admin.site.register(Cad_Cliente, ClienteAdmin)