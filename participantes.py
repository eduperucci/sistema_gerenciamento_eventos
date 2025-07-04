from util_participantes import *
from util import limpar_tela
from dados import lista_eventos, lista_de_participantes


def listar_participantes():
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return
    
    for participante in lista_de_participantes:
        print("-" * 40)
        print("---PARTICIPANTE---")
        print(f"CPF: {participante['cpf']} // NOME: {participante['nome']} // EMAIL: {participante['email']}")

        evento_cadastrado = participante.get('evento_cadastrado') 

        print("\n---EVENTOS CADASTRADOS---")
        if not evento_cadastrado:
            print("Nenhum evento cadastrado")
        elif isinstance(evento_cadastrado, dict):
            print(f"EVENTO: {evento_cadastrado.get('id')} // TEMA: {evento_cadastrado.get('tema')} // NOME: {evento_cadastrado.get('nome')} // DATA: {evento_cadastrado.get('data')}")
        elif isinstance(evento_cadastrado, list):
            for evento in evento_cadastrado:
                print(f"EVENTO: {evento.get('id')} // TEMA: {evento.get('tema')} // NOME: {evento.get('nome')} // DATA: {evento.get('data')}")
        else:
            print("Formato de evento cadastrado inválido.")


        print("-" * 40)


def adicionar_participante():
    print("---Adicionar Participante---")

    while True:
        nome = input("Digite o nome do participante (ou '0' para voltar): ").strip()
        if nome == '0':
            return
        
        email = None

        while True:
            email_tentativa = input("Digite o email do participante (ou '0' para voltar): ").strip().lower()
            if email_tentativa == '0':
                return
            
            if verificar_email_existente(email_tentativa, lista_de_participantes):
                print(f"Email '{email_tentativa}' já cadastrado. Por favor, digite outro email.")
                continue 
            else:
                email = email_tentativa
                break

        
        cpf = None

        while True:
            cpf_tentativa = cadastro_cpf()
            if cpf_tentativa is None:
                return
            
            if verificar_cpf_existente(cpf_tentativa, lista_de_participantes):
                print(f"CPF {cpf_tentativa} já cadastrado. Por favor, digite outro CPF.")
                continue
            else:
                cpf = cpf_tentativa
                break

        evento_cadastrado = evento_do_participante()
        if evento_cadastrado is None:
            print("Seleção de evento cancelada. Cadastro de participante abortado.")
            return

        participantes = {
            "cpf": cpf,
            "nome": nome,   
            "email": email,
            "evento_cadastrado": evento_cadastrado,
        }

        lista_de_participantes.append(participantes)
        print(f"\nParticipante {nome} adicionado com sucesso.")
        
        while True:
            opcao_continuar = input("Deseja adicionar outro participante? (s/n): ").strip().lower()
            if opcao_continuar == 's':
                break
            elif opcao_continuar == 'n':
                return
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")


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


def editar_dados_partipante():
    if not lista_de_participantes:
        print("Nenhum participante cadastrado para editar.")
        return

    while True:
        print("\n=== EDITAR DADOS DO PARTICIPANTE ===")
        print("1. Listar Participantes")
        print("0. Voltar")
        identificador_cpf = input("Digite o CPF do participante que deseja editar (ou '0' para voltar): ").strip()

        if identificador_cpf == '1':
            listar_participantes()
            continue
        elif identificador_cpf == '0':
            return

        if not identificador_cpf.isdigit() or len(identificador_cpf) != 11:
            print("CPF inválido. Deve conter 11 dígitos numéricos. Tente novamente.")
            continue

        participante_a_editar = None

        for participantes in lista_de_participantes:
            if participantes['cpf'] == identificador_cpf:
                participante_a_editar = participantes
                break

        if not participante_a_editar:
            print(f"Participante com CPF '{identificador_cpf}' não encontrado.")
            continue

        print(f"\n---Editando: {participante_a_editar['nome']} (CPF: {participante_a_editar['cpf']})---")
        print("[ENTER] para manter o valor atual.")
        print("Ou digite [0] para cancelar a edição deste participante e voltar.")

        novo_nome = input(f"Nome atual: {participante_a_editar['nome']}. Novo nome (ENTER para manter, '0' para cancelar): ").strip()
        if novo_nome == '0':
            print("Edição de nome cancelada. Saindo da edição deste participante.")
            return
        elif novo_nome != '':
            participante_a_editar['nome'] = novo_nome
            print("Nome atualizado.")

        while True:
            novo_email_input = input(f"Email atual: {participante_a_editar['email']}. Novo email (ENTER para manter, '0' para cancelar): ").strip().lower()
            
            if novo_email_input == '0':
                print("Edição de email cancelada. Saindo da edição deste participante.")
                return
            elif novo_email_input == '':
                break
            
            if verificar_email_existente(novo_email_input, lista_de_participantes) and novo_email_input != participante_a_editar['email'].lower():
                print(f"Erro: Email '{novo_email_input}' já está cadastrado para outro participante. Por favor, digite outro email.")
                continue
            else:
                participante_a_editar['email'] = novo_email_input
                print("Email atualizado.")
                break
        
        print("\nParticipante editado com sucesso!")       
        print("\n--- Dados Atualizados ---")
        print(f"Nome: {participante_a_editar['nome']} // Email: {participante_a_editar['email']} // CPF: {participante_a_editar['cpf']}")

        return