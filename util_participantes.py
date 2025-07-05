from dados import lista_de_participantes, lista_eventos
from eventos import listar_eventos
from util import limpar_tela



def evento_do_participante():
    print("\n--- SELECIONAR EVENTOS PARA O PARTICIPANTE ---")
    
    if not lista_eventos:
        print("\nNenhum evento cadastrado. Não é possível associar eventos.")
        return None

    eventos_escolhidos = []

    while True:
        listar_eventos()
        print("\nDigite o ID do evento para adicionar (pode adicionar múltiplos).")
        print("ENTER. salvar operação")
        print("0. Cancelar Operação")
        
        entrada_usuario = input("\nID do evento: ").strip()

        if entrada_usuario == '0':
            print("\nSeleção de eventos cancelada. O cadastro do participante será abortado.")
            return None


        if entrada_usuario == '':
            if not eventos_escolhidos:
                print("\nVocê deve cadastrar o participante em pelo menos um evento antes de finalizar, ou digite [0] para cancelar.")
                continue
            else:
                print("\nSeleção de eventos finalizada.")
                return eventos_escolhidos
        

        try:
            evento_id = int(entrada_usuario)
        except ValueError:
            print("\nID inválido. Digite um número, '0' para cancelar, ou ENTER para finalizar.")
            continue

        evento_encontrado = None
        for evento in lista_eventos:
            if evento['id'] == evento_id:
                evento_encontrado = evento
                break
        
        if evento_encontrado:
            if evento_encontrado in eventos_escolhidos:
                print(f"\nEvento '{evento_encontrado['nome']}' já foi adicionado a esta seleção.")
            else:
                eventos_escolhidos.append(evento_encontrado)
                print(f"\nEvento '{evento_encontrado['nome']}' adicionado à seleção.")
                print("\nEventos selecionados até agora:")
                for ev in eventos_escolhidos:
                    print(f"  - ID: {ev['id']}, Nome: {ev['nome']}")
        else:
            print(f"\nEvento com ID '{evento_id}' não encontrado. Por favor, digite um ID da lista.")

def verificar_cpf_existente(cpf, lista_de_participantes):
    
    for participante in lista_de_participantes:
        if participante['cpf'] == cpf:
            return True
    return False

def verificar_email_existente(email, lista_de_participantes):
    
    for participante in lista_de_participantes:
        if participante['email'].lower() == email.lower():
            return True

def cadastro_cpf():
    while True:
        cpf = input("Digite seu CPF: ")
        if cpf == '':
            print("\nCPF não digitado")
            continue

        if cpf == '0':
            return None
        
        if not cpf.isdigit() or len(cpf) < 10:
            print("\nCPF inválido: precisa de pelo menos 10 dígitos numéricos.")
            continue
        
        for participante in lista_de_participantes:
            if participante.get("cpf") == cpf:
                print("\nCPF já cadastrado em outro participante.")
                continue
        
        return cpf
        

def buscar_por_cpf():
    if not lista_de_participantes:
        print("\nNenhum participante cadastrado")
        return
    
    while True:
        cpf = input("\nDigite o CPF para busca: ")

        if cpf == '0':
            return None
        
        buscador = list(filter(lambda x: x.get('cpf') == cpf, lista_de_participantes))
        if buscador:
            participante = buscador[0]
            print("   \n-Participante encontrado-")
            print(f"   CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']} ")
            return participante
            

def buscar_por_nome():
    if not lista_de_participantes:
        print("\nNenhum participante cadastrado")
        return
    
    while True:
        nome = input("\nDigite o nome para busca: ").strip().lower()

        if nome == '0':
            return None
        
        buscador = list(filter(lambda x: x.get('nome').lower() == nome, lista_de_participantes))
        if buscador:
            participante = buscador[0]
            print("   \n---Participante encontrado---")
            print(f"   CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']}")
            return participante

    
def buscar_por_email():
    if not lista_de_participantes:
        print("\nNenhum participante cadastrado")
        return
    
    while True:
        email = input("\nDigite o nome para busca: ").strip().lower()

        if email == '0':
            return None
        
        buscador = list(filter(lambda x: x.get('email').lower() == email, lista_de_participantes))
        if buscador:
            participante = buscador[0]
            print("   \n---Participante encontrado---")
            print(f"   CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']}")
            return participante