from datetime import datetime

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

    
def gerar_id_reutilizavel(lista):
    ids_em_uso = {x['id'] for x in lista}
    novo_id = 1
    while novo_id in ids_em_uso:
        novo_id += 1
    return novo_id
