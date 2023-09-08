from django.contrib import admin
from .models import Curso_info,Curso_Api,Curso_Ali


@admin.register(Curso_info)
class Curso_infoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_criacao', 'descricao', 'imagem')

@admin.register(Curso_Ali)
class Curso_AliAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_criacao', 'descricao', 'imagem')

@admin.register(Curso_Api)
class Curso_ApiAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_criacao', 'descricao', 'imagem')
