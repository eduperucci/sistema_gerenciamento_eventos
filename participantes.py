from util import corrigir_id_duplicados, gerar_id
from funcoes_participantes import temas_de_interesse, cadastro_cpf
from dados import lista_eventos, lista_de_participantes

corrigir_id_duplicados(lista_de_participantes)

def listar_participantes():
    for participante in lista_de_participantes:
        print(f"CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']} // TEMAS DE INTERESSE: {participante['temas']} }}")
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
  
    temas_ecolhidos = temas_de_interesse()



    partipantes = {
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "temas": temas_ecolhidos,
    }

    lista_de_participantes.append(partipantes)
    print(f"\nParticipante {nome} adicionado com sucesso.")
    return


def remover_participante(): pass


def editar_dados_partipante(): pass


def agrupar_eventos(): pass