from util_participantes import *
from dados import lista_eventos, lista_de_participantes


def listar_participantes():
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return
    
    for participante in lista_de_participantes:
        print("-" * 40)
        print("---PARTICIPANTE---")
        print(f"\nCPF: {participante['cpf']}\nOME: {participante['nome']},\nEMAIL: {participante['email']}")

        evento_cadastrado = participante.get('evento_cadastrado') 

        print("\n---EVENTOS CADASTRADOS---")
        if not evento_cadastrado:
            print("Nenhum evento cadastrado")
        elif isinstance(evento_cadastrado, dict):
            print(f"\nEVENTO: {evento_cadastrado.get('id')}\nTEMA: {evento_cadastrado.get('tema')},\nNOME: {evento_cadastrado.get('nome')},\nDATA: {evento_cadastrado.get('data')}")
        elif isinstance(evento_cadastrado, list):
            for evento in evento_cadastrado:
                print(f"\nEVENTO: {evento.get('id')}, \nTEMA: {evento.get('tema')},\nNOME: {evento.get('nome')},\nDATA: {evento.get('data')}")
        else:
            print("Formato de evento cadastrado inválido.")


        print("-" * 40)


def adicionar_participante():
    print("---Adcionar Participante---")
    nome = input("Digite o nome do participante: ").strip()
    if nome == '0':
        return
    
    email = input("Digite o email do participante: ").strip().lower()
    if email == '0':
        return
    
    cpf = cadastro_cpf()
    if cpf is None:
        return

    evento_cadastrado = evento_do_participante() 

    participantes = {
        "cpf": cpf,
        "nome": nome,   
        "email": email,
        "evento_cadastrado": evento_cadastrado,
    }

    lista_de_participantes.append(participantes)
    print(f"\nParticipante {nome} adicionado com sucesso.")
    return


def remover_participante():
    if not lista_de_participantes:
        print("Participantes não cadastrados")
        return
    
    while True:
        print("\n---Remover Participante---")
        print("1. Listar Participantes")
        print("0. Voltar")

        acao = input("Digite o CPF ou email do participante para remover: ").strip()

        if acao == '1':
            listar_participantes()
        elif acao == '0':
            return
        else:
            participante_a_remover = None
            for participante in lista_de_participantes:
                if participante['cpf'] == acao or participante['email'].lower() == acao.lower():
                    participante_a_remover = participante
                    break

            if participante_a_remover:
                lista_de_participantes.remove(participante_a_remover)
                print(f"Participante '{participante_a_remover['nome']}' removido com sucesso!")
                return
            else:
                print(f"Participante com CPF ou email '{acao}' não encontrado.")


def editar_dados_partipante(): pass