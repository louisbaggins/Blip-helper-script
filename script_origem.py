import sys
import json

if len(sys.argv) < 2:
    print('uso: python script_origem.py <arquivo>')
    exit(-1)

arquivo_entrada = open(sys.argv[1], 'r', encoding='utf8')
fluxo = json.load(arquivo_entrada)
arquivo_entrada.close()

for bloco in fluxo:
    try:
        fluxo[bloco]['$contentActions'][-1]['input']['bypass']
    except:
        continue

    if not fluxo[bloco]['$contentActions'][-1]['input']['bypass']:
        fluxo[bloco]['$leavingCustomActions'].append({
                "type": "SetVariable",
                "$title": 'Define origem',
                "$invalid": False,
                "settings": {
                    "variable": "Origem",
                    "value": fluxo[bloco]['$title']
                },
                 "conditions": []
            })
        fluxo[bloco]['$tags'].append({
            'background': '#FF4A1E',
            'label': 'SetVariable',
            'id': 'blip-tag-4abb0969-91dd-7fcf-40c2-8951445063f6',
            'canChangeBackground': False
        })
        
nome_saida = '%s OrigemVariable.json' % (sys.argv[1].split('.')[0])
arquivo_saida = open(nome_saida, 'w', encoding='utf8')
arquivo_saida.write(json.dumps(fluxo))
arquivo_saida.close()

print('Feito! Salvo no arquivo %s' % nome_saida)
