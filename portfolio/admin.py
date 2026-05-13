from django.contrib import admin
from .models import (Tecnologia, Competencia, Formacao, Docente,
                      Licenciatura, UnidadeCurricular, TFC, Projeto, MakingOf)


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'interesse', 'site')
    search_fields = ('nome',)
    list_filter = ('interesse',)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    search_fields = ('nome',)
    list_filter = ('tipo', 'nivel')


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
    list_display = ('nome', 'sigla', 'instituicao', 'duracao', 'ects_total')
    search_fields = ('nome', 'sigla')


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'ano_curricular', 'semestre', 'ects', 'docente')
    search_fields = ('nome', 'codigo')
    list_filter = ('ano_curricular', 'semestre', 'licenciatura', 'docente')


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'orientadores', 'rating')
    search_fields = ('titulo', 'autores', 'palavras_chave')
    list_filter = ('rating',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_curricular', 'link_github')
    search_fields = ('nome',)
    list_filter = ('unidade_curricular',)
    filter_horizontal = ('tecnologias', 'competencias')


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('entidade', 'descricao')
    search_fields = ('entidade',)