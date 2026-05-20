from django.urls import path
from . import views

app_name = "artigos"

urlpatterns = [
    path('', views.artigos_view, name="artigos"),
    path('<int:id>/', views.artigo_detalhe_view, name="detalhe"),
    path('novo/', views.artigo_criar_view, name="criar"),
    path('editar/<int:id>/', views.artigo_editar_view, name="editar"),
    path('like/<int:id>/', views.artigo_like_view, name="like"),
]
