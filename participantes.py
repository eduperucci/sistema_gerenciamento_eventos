from util_participantes import *
from util import limpar_tela, enter_continuar
from dados import lista_eventos, lista_de_participantes, salvar_dados, PARTICIPANTES_FILE


def listar_participantes_opcoes():
    limpar_tela()
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return


    for participante in lista_de_participantes:
        print("-" * 60)
        print("---PARTICIPANTE---")
        print(f"CPF: {participante['cpf']} | NOME: {participante['nome']} | EMAIL: {participante['email']}")

        evento_cadastrado = participante.get('evento_cadastrado') 

        print("\n-Eventos Cadastrados-")
        if not evento_cadastrado:
            print("   Nenhum evento cadastrado")
        elif isinstance(evento_cadastrado, dict):
            print(f"   EVENTO: {evento_cadastrado.get('id')} | TEMA: {evento_cadastrado.get('tema')} | NOME: {evento_cadastrado.get('nome')} | DATA: {evento_cadastrado.get('data')}")
            print("-" * 60)
        elif isinstance(evento_cadastrado, list):
            for evento in evento_cadastrado:
                print(f"   EVENTO: {evento.get('id')} | TEMA: {evento.get('tema')} | NOME: {evento.get('nome')} | DATA: {evento.get('data')}")
                print("-" * 60)
        else:
            print("Formato de evento cadastrado inválido.")
    enter_continuar()

def listar_participantes():
    limpar_tela()
    if not lista_de_participantes:
        print("Nenhum participante cadastrado")
        return


    for participante in lista_de_participantes:
        print("-" * 40)
        print("---PARTICIPANTE---")
        print(f"CPF: {participante['cpf']} | NOME: {participante['nome']} | EMAIL: {participante['email']}")

        evento_cadastrado = participante.get('evento_cadastrado') 

        print("\n-Eventos Cadastrados-")
        if not evento_cadastrado:
            print("   Nenhum evento cadastrado")
        elif isinstance(evento_cadastrado, dict):
            print(f"   EVENTO: {evento_cadastrado.get('id')} | TEMA: {evento_cadastrado.get('tema')} | NOME: {evento_cadastrado.get('nome')} | DATA: {evento_cadastrado.get('data')}")
        elif isinstance(evento_cadastrado, list):
            for evento in evento_cadastrado:
                print(f"   EVENTO: {evento.get('id')} | TEMA: {evento.get('tema')} | NOME: {evento.get('nome')} | DATA: {evento.get('data')}")
        else:
            print("   Formato de evento cadastrado inválido.")


def adicionar_participante():
    limpar_tela()
    print("---Adicionar Participante---")

    while True:
        nome = input("\nDigite o nome do participante [0] para voltar): ").strip()
        if nome == '0':
            return
        
        email = None

        while True:
            email_tentativa = input("\nDigite o email do participante [0] para voltar: ").strip().lower()
            if email_tentativa == '0':
                return
            
            if verificar_email_existente(email_tentativa, lista_de_participantes):
                print(f"\nEmail '{email_tentativa}' já cadastrado. Por favor, digite outro email.")
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
                print(f"\nCPF {cpf_tentativa} já cadastrado. Por favor, digite outro CPF.")
                continue
            else:
                cpf = cpf_tentativa
                break

        evento_cadastrado = evento_do_participante()
        if evento_cadastrado is None:
            print("\nSeleção de evento cancelada. Cadastro de participante abortado.")
            return

        participantes = {
            "cpf": cpf,
            "nome": nome,   
            "email": email,
            "evento_cadastrado": evento_cadastrado,
        }

        lista_de_participantes.append(participantes)
        salvar_dados(PARTICIPANTES_FILE, lista_de_participantes)
        print(f"\nParticipante {nome} adicionado com sucesso.")
        
        while True:
            opcao_continuar = input("\nDeseja adicionar outro participante? (s/n): ").strip().lower()
            if opcao_continuar == 's':
                break
            elif opcao_continuar == 'n':
                return
            else:
                print("\nOpção inválida. Digite 's' para sim ou 'n' para não.")


def remover_participante():
    limpar_tela()
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
                salvar_dados(PARTICIPANTES_FILE, lista_de_participantes) # Adicione esta linha
                print(f"Participante '{participante_a_remover['nome']}' removido com sucesso!")
                return
            else:
                print(f"Participante com CPF ou email '{acao}' não encontrado.")


def editar_dados_partipante():
    limpar_tela()
    if not lista_de_participantes:
        print("Nenhum participante cadastrado para editar.")
        return

    while True:
        print("\n---EDITAR DADOS DO PARTICIPANTE---")
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
            salvar_dados(PARTICIPANTES_FILE, lista_de_participantes)
            print("Nome atualizado.")

        while True:
            novo_email_input = input(f"Email atual: {participante_a_editar['email']}. Novo email (ENTER para manter, '0' para cancelar): ").strip().lower()
            
            if novo_email_input == '0':
                print("Edição de email cancelada. Saindo da edição deste participante.")
                return
            elif novo_email_input == '':
                break
            

            if '@' not in novo_email_input:
                print("Erro: O email deve conter o caractere '@'. Por favor, digite um email válido.")
                continue

            if verificar_email_existente(novo_email_input, lista_de_participantes) and novo_email_input != participante_a_editar['email'].lower():
                print(f"Erro: Email '{novo_email_input}' já está cadastrado para outro participante. Por favor, digite outro email.")
                continue
            else:
                participante_a_editar['email'] = novo_email_input
                salvar_dados(PARTICIPANTES_FILE, lista_de_participantes)
                print("Email atualizado.")
                break
        
        print("\nParticipante editado com sucesso!")       
        print("\n--- Dados Atualizados ---")
        print(f"Nome: {participante_a_editar['nome']} | Email: {participante_a_editar['email']} | CPF: {participante_a_editar['cpf']}")

        return