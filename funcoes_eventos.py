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