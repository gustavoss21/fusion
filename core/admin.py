from django.contrib import admin
from .models import Cargo,Funcionario,Servico,Features

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo',)

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','bio','faceboock','instagram','instagram')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','descricao','icone')

@admin.register(Features)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('feature','descricao','icone')