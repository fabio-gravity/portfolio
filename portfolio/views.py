from django.shortcuts import render
from .models import (Tecnologia, Competencia, Formacao, Docente,
                      Licenciatura, UnidadeCurricular, TFC, Projeto, MakingOf)


def index_view(request):
    return render(request, 'portfolio/index.html')


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