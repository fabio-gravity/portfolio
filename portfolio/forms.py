from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'tecnologias', 'competencias',
                  'unidade_curricular', 'imagem', 'link_github']
        widgets = {
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'descricao', 'logo', 'site', 'interesse']


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'descricao', 'tipo', 'nivel']


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['nome', 'instituicao', 'descricao', 'data_inicio',
                  'data_fim', 'certificado_url']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }