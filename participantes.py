from util_participantes import *
from dados import lista_eventos, lista_de_participantes

lista_de_participantes = []

def listar_participantes():
    for participante in lista_de_participantes:
        print(f"\nCPF: {participante['cpf']}\nNOME: {participante['nome']}\nEMAIL: {participante['email']}\nEVENTOS CADASTRADOS: {participante['evento_cadastrado']}")
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")


def buscar_participante(): pass


def adicionar_participante():
    nome = input("Digite o nome do participante: ")
    if nome == '0':
        return
    
    email = input("Digite o email do participante: ")
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


def remover_participante(): pass


def editar_dados_partipante(): pass


def agrupar_eventos(): pass