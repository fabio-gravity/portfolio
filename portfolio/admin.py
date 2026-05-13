from django.contrib import admin
from django.contrib import admin
from .models import Tecnologia,Competencia,Formacao,Docente,Licenciatura,UnidadeCurricular,TFC,Projeto,MakingOf


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'interesse', 'site')
    search_fields = ('nome',)
    list_filter = ('interesse',)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    search_fields = ('nome',)
    list_filter = ('nivel',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'data_inicio', 'data_fim')
    search_fields = ('nome', 'instituicao')
    list_filter = ('instituicao',)
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'pagina')
    search_fields = ('nome', 'email')

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'duracao', 'ano_inicio')
    search_fields = ('nome', 'instituicao')
 
@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'docente', 'licenciatura')
    search_fields = ('nome', 'codigo')
    list_filter = ('licenciatura', 'docente')

 
@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('nome', 'licenciatura', 'classificacao', 'data_inicio', 'data_fim')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link_github')
    search_fields = ('nome',)
    filter_horizontal = ('tecnologias', 'competencias')

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('entidade', 'descricao')
    search_fields = ('entidade',)