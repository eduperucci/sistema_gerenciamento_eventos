from dados import lista_de_participantes, lista_eventos

def temas_de_interesse():
    print("\n====TEMAS DISPONÍVEIS====")
    if not lista_eventos:
        print("\nNenhum tema cadastrado")
        return
    
    temas_unicos = set()

    for evento in lista_eventos:
        temas_unicos.add(evento['tema'].strip())

    temas_ordenados = sorted(temas_unicos)
    
    for i, tema in enumerate(temas_ordenados):
        print(f'{i+1}. {tema}')

    temas_selecionados = []

    while True:
        escolha = input("\nDigite o número do tema de interesse ou pressione [Enter] para terminar: ").strip()

        if escolha == '':
            print("Salvo.")
            break

        try:
            escolha_int = int(escolha)
            if 1 <= escolha_int <= len(temas_ordenados):
                tema_escolhido = temas_ordenados[escolha_int - 1]
                if tema_escolhido not in temas_selecionados:
                    temas_selecionados.append(tema_escolhido)
                    print(f"'{tema_escolhido}' adicionado aos temas de interesse.")
                else:
                    print("Tema já selecionado anteriormente.")
            else:
                print("Número fora do intervalo, tente novamente.")
        except ValueError:
            print("Número inválido, digite apenas números ou pressione [Enter] para salvar.")

    if not temas_selecionados:
        return "Nehum tema selecionado"
    return temas_selecionados

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