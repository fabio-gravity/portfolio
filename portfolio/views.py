from django.shortcuts import render, redirect, get_object_or_404
from .models import (Tecnologia, Competencia, Formacao, Docente,
                      Licenciatura, UnidadeCurricular, TFC, Projeto, MakingOf)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


# === INDEX ===

def index_view(request):
    return render(request, 'portfolio/index.html')


# === SOBRE ===

def sobre_view(request):
    return render(request, 'portfolio/sobre.html')


# === LISTAGENS ===

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all().order_by('-interesse')
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('docente', 'licenciatura').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})


def tfcs_view(request):
    tfcs = TFC.objects.all().order_by('-rating')
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def makingof_view(request):
    entradas = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'entradas': entradas})


# === CRUD PROJETOS ===

def projeto_criar_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Novo Projeto'})


def projeto_editar_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto'})


def projeto_apagar_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/confirmar_apagar.html',
                  {'objeto': projeto, 'tipo': 'Projeto', 'voltar_url': 'portfolio:projetos'})


# === CRUD TECNOLOGIAS ===

def tecnologia_criar_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:tecnologias')
    else:
        form = TecnologiaForm()
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Nova Tecnologia'})


def tecnologia_editar_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'portfolio/tecnologia_form.html', {'form': form, 'titulo': 'Editar Tecnologia'})


def tecnologia_apagar_view(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html',
                  {'objeto': tecnologia, 'tipo': 'Tecnologia', 'voltar_url': 'portfolio:tecnologias'})


# === CRUD COMPETENCIAS ===

def competencia_criar_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm()
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Nova Competência'})


def competencia_editar_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    return render(request, 'portfolio/competencia_form.html', {'form': form, 'titulo': 'Editar Competência'})


def competencia_apagar_view(request, id):
    competencia = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        competencia.delete()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/confirmar_apagar.html',
                  {'objeto': competencia, 'tipo': 'Competência', 'voltar_url': 'portfolio:competencias'})


# === CRUD FORMACOES ===

def formacao_criar_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:formacoes')
    else:
        form = FormacaoForm()
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Nova Formação'})


def formacao_editar_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('portfolio:formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    return render(request, 'portfolio/formacao_form.html', {'form': form, 'titulo': 'Editar Formação'})


def formacao_apagar_view(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('portfolio:formacoes')
    return render(request, 'portfolio/confirmar_apagar.html',
                  {'objeto': formacao, 'tipo': 'Formação', 'voltar_url': 'portfolio:formacoes'})