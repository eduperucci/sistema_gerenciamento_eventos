from util_participantes import *
from dados import lista_eventos, lista_de_participantes


def listar_participantes():
    for participante in lista_de_participantes:
        print(f"\nCPF: {participante['cpf']}\nNOME: {participante['nome']}\nEMAIL: {participante['email']}\nEVENTOS CADASTRADOS: {participante['evento_cadastrado']}")
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")

def adicionar_participante():
    print("---Adcionar Participante---")
    nome = input("Digite o nome do participante: ")
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
        print("\n---Remover Participante")
        print("1. Listar Participantes")
        print("0. voltar")

        acao = input("Digite o nome, cpf ou email para remover: ")
        if acao == '1':
            listar_participantes()
        elif acao == '0':
            return
        else:
            for participante in lista_de_participantes:
                if participante['cpf'] == acao or participante['nome'] == acao or participante['email'] == acao:
                    lista_de_participantes.remove(participante)
                    print(f"Parcipante {participante['nome']} removido ")
        

    







def editar_dados_partipante(): pass