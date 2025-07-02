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