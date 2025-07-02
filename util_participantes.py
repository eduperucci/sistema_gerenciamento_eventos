from dados import lista_de_participantes, lista_eventos
from eventos import listar_eventos

def evento_do_participante():
    print("\n---CADASTRAR EVENTOS---")
    while True:
        if not lista_eventos:
            print("\nNenhum tema cadastrado")
            return
        else:
            listar_eventos()
            try:
                evento_escolhido = int(input("Digite o ID do evento para cadastrar: "))
            except ValueError:
                print("ID inválido digite apenas núemeros")
                continue

            if evento_escolhido == 0:
                return
            
            for evento in lista_eventos:
                if evento['id'] == evento_escolhido:
                    formatacao = (f"\n Evento:{evento['id']} \n Tema: {evento['tema']} \n Nome:{evento['nome']}\n Data:{evento['data']}")
                    return formatacao

def cadastro_cpf():
    while True:
        cpf = input("Digite seu cpf: ")
        if cpf == '':
            print("CPF não digitado")
            continue

        if cpf == '0':
            return None
        
        if not cpf.isdigit() or len(cpf) < 10:
            print("CPF inválido: precisa de pelo menos 10 dígitos numéricos.")
            continue
        
        for participante in lista_de_participantes:
            if participante.get("cpf") == cpf:
                print("CPF já cadastrado em outro participante.")
                continue
        
        return cpf
        

def buscar_por_cpf():

    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return
    
    while True:
        cpf = input("Digite o cpf para busca: ")

        if cpf == '0':
            return None
        
        for participante in lista_de_participantes:
            if participante.get('cpf') == cpf:
                print("---Participante encontrado---")
                print(f"CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']} // TEMAS DE INTERESSE: {participante['temas']}")
                return participante
            
def buscar_por_nome(): pass

def buscar_por_email(): pass