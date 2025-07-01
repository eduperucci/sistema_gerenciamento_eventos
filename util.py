from datetime import datetime
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 
limpar_tela()


def ler_data():
    while True:
        data_digitada = input("Difina a nova data do evento (DD/MM/AAAA): ").strip()
        if data_digitada == '0':
            return
        
        try:
            data = datetime.strptime(data_digitada, "%d/%m/%Y").date()            
            return data.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida, tento novamente com os padrões DD/MM/AAAA")

    
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



