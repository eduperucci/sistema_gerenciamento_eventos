from datetime import datetime
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 
limpar_tela()


def ler_data():
    while True:
        data_digitada = input("Digite data do evento (DD/MM/AAAA): ").strip()
        if data_digitada == '0':
            return
        
        try:
            data = datetime.strptime(data_digitada, "%d/%m/%Y").date()            
            return data.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida, tento novamente com os padrões DD/MM/AAAA")



