from django.contrib import admin
from .models import Artigo, Like, Comentario


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'total_likes')
    search_fields = ('titulo', 'texto')
    list_filter = ('autor', 'data_criacao')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'data')
    list_filter = ('autor',)


admin.site.register(Like)
