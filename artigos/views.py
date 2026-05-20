from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.groups.filter(name='autores').exists()


# === LISTAGEM ===

def artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/artigos.html', {
        'artigos': artigos,
        'is_autor': request.user.is_authenticated and is_autor(request.user),
    })


# === DETALHE + COMENTÁRIOS ===

def artigo_detalhe_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.all()
    form = ComentarioForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('artigos:detalhe', id=artigo.id)

    return render(request, 'artigos/artigo_detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form,
        'is_autor': request.user.is_authenticated and is_autor(request.user),
    })


# === CRIAR ===

@login_required(login_url='/accounts/login/')
def artigo_criar_view(request):
    if not is_autor(request.user):
        return redirect('artigos:artigos')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigos:artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Novo Artigo'})


# === EDITAR ===

@login_required(login_url='/accounts/login/')
def artigo_editar_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if artigo.autor != request.user:
        return redirect('artigos:artigos')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhe', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Editar Artigo'})


# === LIKE ===

def artigo_like_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    like, created = Like.objects.get_or_create(artigo=artigo, session_key=session_key)

    if not created:
        like.delete()

    return redirect('artigos:detalhe', id=artigo.id)
