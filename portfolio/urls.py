from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('sobre/', views.sobre_view, name="sobre"),

    # Listagens
    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('competencias/', views.competencias_view, name="competencias"),
    path('formacoes/', views.formacoes_view, name="formacoes"),
    path('docentes/', views.docentes_view, name="docentes"),
    path('licenciaturas/', views.licenciaturas_view, name="licenciaturas"),
    path('ucs/', views.ucs_view, name="ucs"),
    path('tfcs/', views.tfcs_view, name="tfcs"),
    path('projetos/', views.projetos_view, name="projetos"),
    path('makingof/', views.makingof_view, name="makingof"),

    # CRUD Projetos
    path('projetos/novo/', views.projeto_criar_view, name="projeto_criar"),
    path('projetos/editar/<int:id>/', views.projeto_editar_view, name="projeto_editar"),
    path('projetos/apagar/<int:id>/', views.projeto_apagar_view, name="projeto_apagar"),

    # CRUD Tecnologias
    path('tecnologias/nova/', views.tecnologia_criar_view, name="tecnologia_criar"),
    path('tecnologias/editar/<int:id>/', views.tecnologia_editar_view, name="tecnologia_editar"),
    path('tecnologias/apagar/<int:id>/', views.tecnologia_apagar_view, name="tecnologia_apagar"),

    # CRUD Competencias
    path('competencias/nova/', views.competencia_criar_view, name="competencia_criar"),
    path('competencias/editar/<int:id>/', views.competencia_editar_view, name="competencia_editar"),
    path('competencias/apagar/<int:id>/', views.competencia_apagar_view, name="competencia_apagar"),

    # CRUD Formacoes
    path('formacoes/nova/', views.formacao_criar_view, name="formacao_criar"),
    path('formacoes/editar/<int:id>/', views.formacao_editar_view, name="formacao_editar"),
    path('formacoes/apagar/<int:id>/', views.formacao_apagar_view, name="formacao_apagar"),
]