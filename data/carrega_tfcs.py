"""
Script para carregar os dados dos TFCs a partir do ficheiro JSON.
Executar a partir da raiz do projeto:
    python data/carrega_tfcs.py
"""

import os
import sys
import json
import django

# Adicionar a raiz do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC


def carregar_tfcs():
    # Caminho para o ficheiro JSON
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tfcs_2025_.json')

    # Ler o ficheiro JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        tfcs_data = json.load(f)

    print(f"Encontrados {len(tfcs_data)} TFCs no ficheiro JSON.")

    criados = 0
    existentes = 0

    for tfc_data in tfcs_data:
        # Verificar se já existe (pelo titulo)
        tfc, created = TFC.objects.get_or_create(
            titulo=tfc_data.get('titulo', ''),
            defaults={
                'autores': tfc_data.get('autores', ''),
                'orientadores': tfc_data.get('orientadores', ''),
                'licenciaturas': tfc_data.get('licenciaturas', ''),
                'sumario': tfc_data.get('sumario', ''),
                'link_pdf': tfc_data.get('link_pdf', ''),
                'imagem': tfc_data.get('imagem', ''),
                'palavras_chave': tfc_data.get('palavras_chave', ''),
                'areas': tfc_data.get('areas', ''),
                'tecnologias_usadas': tfc_data.get('tecnologias_usadas', ''),
                'rating': tfc_data.get('rating', 0),
            }
        )

        if created:
            criados += 1
            print(f"  ✓ Criado: {tfc.titulo[:60]}...")
        else:
            existentes += 1
            print(f"  - Já existe: {tfc.titulo[:60]}...")

    print(f"\nResultado: {criados} criados, {existentes} já existiam.")


if __name__ == '__main__':
    carregar_tfcs()
