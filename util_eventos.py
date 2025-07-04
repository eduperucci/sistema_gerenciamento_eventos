from dados import lista_eventos
from util import limpar_tela, ler_data

def eventos_na_mesma_data(tema, nome, data, lista):
    tema = tema.strip().lower()
    nome = nome.strip().lower()
    data = data.strip()
    return any(
        evento['tema'].strip().lower() == tema and
        evento['nome'].strip().lower() == nome and
        evento['data'].strip() == data
        for evento in lista
    )

def gerar_id(lista):
    ids_em_uso = {x['id'] for x in lista}
    novo_id = 1
    while novo_id in ids_em_uso:
        novo_id += 1
    return novo_id

def corrigir_id_duplicados(lista):
    vistos = set()
    for evento in lista:
        id_atual = evento["id"]
        if id_atual in vistos:
            novo_id = gerar_id(lista)
            evento["id"] = novo_id
        vistos.add(evento["id"])

def buscar_por_tema():
    if not lista_eventos:
        print("Nenhum evento cadastrado")
        return
    
    while True:
        tema = input("Digite o tema do evento [0] para voltar: ").strip().lower()
        
        if tema == '0':
            return

        buscador = list(filter(lambda x: x.get('tema').strip().lower() == tema, lista_eventos))
        if buscador:
            print("---Eventos encontrados por tema---")
            for evento in buscador:
                print(f"ID: {evento['id']} // TEMA: {evento['tema']} // NOME: {evento['nome']} // DATA: {evento['data']}")
            return
        else:
            print(f"Nenhum evento encontrado com o tema '{tema}'. Tente novamente ou digite '0' para voltar.")
            continue

def buscar_por_nome():
    if not lista_eventos:
        print("Nenhum evento cadastrado")
        return
    
    while True:
        nome = input("Digite o nome do evento (ou '0' para voltar): ").strip().lower()
        if nome == '0':
            return
        
        buscador = list(filter(lambda x: x.get('nome').strip().lower() == nome, lista_eventos))
        if buscador:
            print("---Eventos encontrados por nome---")
            for evento in buscador:
                print(f"ID: {evento['id']} // TEMA: {evento['tema']} // NOME: {evento['nome']} // DATA: {evento['data']}")
            return
        else:
            print(f"Nenhum evento encontrado com o nome '{nome}'. Tente novamente ou digite '0' para voltar.")
            continue

def buscar_por_data():
    if not lista_eventos:
        print("Nenhum evento cadastrado")
        return
    
    while True:
        data = ler_data()
        if data == '0':
            return
        
        buscador = list(filter(lambda x: x.get('data').strip() == data, lista_eventos))
        if buscador:
            print("---Eventos encontrados por data---")
            for evento in buscador:
                print(f"ID: {evento['id']} // TEMA: {evento['tema']} // NOME: {evento['nome']} // DATA: {evento['data']}")
            return
        else:
            print(f"Nenhum evento encontrado na data '{data}'. Tente novamente ou digite '0' para voltar.")
            continue