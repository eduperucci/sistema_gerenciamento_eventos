import json

PARTICIPANTES_FILE = 'participantes.json'
EVENTOS_FILE = 'eventos.json'

lista_de_participantes = [
    {
        "cpf": "27799974812",
        "nome": "Leandro",
        "email": "leandro@gmail.com", 
        "evento_cadastrado": {
            'id': 1,
            'tema': 'Inteligência Artificial',
            'nome': 'Smart Homes',
            'data': '15/02/2025'}
            }
    ]

lista_eventos = [
    {"id": 1,
    "tema": "Inteligência Artificial",
    "nome": "Smart Home",
    "data": "15/02/2025"},

    {"id": 3,
    "tema": "Web",
    "nome": "HTML avançado", 
    "data": "15/02/2025"},

    {"id": 3,
    "tema": "Segurança",
    "nome": "Criptografia em Android's", 
    "data": "15/02/2025"}
    ]


def salvar_dados(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)