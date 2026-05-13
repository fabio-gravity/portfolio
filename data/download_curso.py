"""
Script para descarregar os dados do curso LEI e das UCs da API da Lusófona.
Executar a partir da raiz do projeto:
    python data/download_curso.py

Necessita: pip install requests
"""

import requests
import json
import os

# Criar pasta files/ dentro de data/ se não existir
files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
os.makedirs(files_dir, exist_ok=True)

schoolYear = '202526'
course = 260  # LEI

for language in ['PT', 'ENG']:

    # 1. Descarregar dados do curso
    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    payload = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }
    headers = {'content-type': 'application/json'}

    print(f"A descarregar curso LEI ({language})...")
    response = requests.post(url, json=payload, headers=headers)
    response_dict = response.json()

    filepath = os.path.join(files_dir, f"ULHT{course}-{language}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(response_dict, f, indent=4)
    print(f"  ✓ Guardado: {filepath}")

    # 2. Descarregar dados de cada UC
    for uc in response_dict.get('courseFlatPlan', []):
        url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
        payload_uc = {
            'language': language,
            'curricularIUnitReadableCode': uc['curricularIUnitReadableCode'],
        }

        print(f"  A descarregar UC: {uc.get('curricularIUnitReadableCode')} ({language})...")
        response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
        response_uc_dict = response_uc.json()

        filepath_uc = os.path.join(files_dir, f"{uc['curricularIUnitReadableCode']}-{language}.json")
        with open(filepath_uc, "w", encoding="utf-8") as f:
            json.dump(response_uc_dict, f, indent=4)

    print(f"  ✓ Todas as UCs ({language}) descarregadas.")

print("\n✓ Download completo! Ficheiros guardados em data/files/")
print("Próximo passo: python data/carrega_curso.py")
