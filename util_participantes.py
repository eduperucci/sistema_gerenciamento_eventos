from dados import lista_de_participantes, lista_eventos
from eventos import listar_eventos

def evento_do_participante():
    print("\n---CADASTRAR EVENTOS---")
    print("0. Cancelar")
    if not lista_eventos:
        print("\nNenhum evento cadastrado")
        return

    eventos_escolhidos = []

    while True:
        listar_eventos()
        evento_escolhido = input("Digite o ID do evento para cadastrar: ")

        if evento_escolhido == '':
            break
        
        if evento_escolhido == '0':
            break

        try:
            evento_escolhido = int(evento_escolhido)
        except ValueError:
            print("ID inválido. Digite apenas números.")
            continue

        for evento in lista_eventos:
            if evento['id'] == evento_escolhido:
                if evento in eventos_escolhidos:
                    print("Evento já cadastrado.")
                else:
                    eventos_escolhidos.append(evento)
                    print(f"Evento {evento['nome']} cadastrado com sucesso")
                    formatacao = (f"\n Evento:{evento['id']} \n Tema: {evento['tema']} \n Nome:{evento['nome']}\n Data:{evento['data']}")
                    print(formatacao)
                break
        else:
            print("ID de evento inválido, tente novamente.")

    return eventos_escolhidos


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
        cpf = input("Digite o CPF para busca: ")

        if cpf == '0':
            return None
        
        buscador = list(filter(lambda x: x.get('cpf') == cpf, lista_de_participantes))
        if buscador:
            participante = buscador[0]
            print("---Participante encontrado---")
            print(f"CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']} // TEMAS DE INTERESSE: {participante['temas']}")
            return participante
            

def buscar_por_nome():
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return
    
    while True:
        nome = input("Digite o nome para busca: ").strip().lower()

        if nome == '0':
            return None
        
        buscador = list(filter(lambda x: x.get('nome').lower() == nome, lista_de_participantes))
        if buscador:
            participante = buscador[0]
            print("---Participante encontrado---")
            print(f"CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']} // TEMAS DE INTERESSE: {participante['temas']}")
            return participante

    
def buscar_por_email():
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return
    
    while True:
        email = input("Digite o nome para busca: ").strip().lower()

        if email == '0':
            return None
        
        buscador = list(filter(lambda x: x.get('email').lower() == email, lista_de_participantes))
        if buscador:
            participante = buscador[0]
            print("---Participante encontrado---")
            print(f"CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']} // TEMAS DE INTERESSE: {participante['temas']}")
            return participante