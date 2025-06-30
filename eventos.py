from funcoesextras import ler_data, gerar_id_reutilizavel

lista_eventos = [
    {"id": 1, "tema": "Inteligência Artificial", "nome": "Smart Homes", "data": "15/02/2025"},
    {"id": 2, "tema": "Inteligência Artificial", "nome": "Vão roubar nossos empregos", "data": "15/02/2025"},
    {"id": 2, "tema": "Web", "nome": "HTML avaçado", "data": "15/02/2025"}
    ]

def exibir_eventos():
    print("\n====EVENTOS DISPONÍVEIS====")

    if not lista_eventos:
        print("\nNenhum evento cadastrado")

    listar_eventos() 


def listar_eventos():
    for evento in lista_eventos:
        print(f"ID: {evento['id']} // TEMA: {evento['tema']} // NOME: {evento['nome']} // DATA: {evento['data']}")


def adicionar_evento():
    while True:
        print("\n====ADICIONAR EVENTOS OPÇÕES====")
        print("0. Voltar\n")

        tema_dig = input("Digite o tema do evento: ")
        if tema_dig == '0':
            return
        
        nome_dig = input("Digite o nome do evento: ")
        if nome_dig == '0':
            return

        data_dig = ler_data()
        id_gerado = gerar_id_reutilizavel(lista_eventos)

        eventos = {
            "id": id_gerado,    
            "tema": tema_dig,
            "nome": nome_dig,
            "data": data_dig
        }
        
        lista_eventos.append(eventos)
        print(f"\nEvento {tema_dig} criado com sucesso.")
        return


def remover_evento():
    while True:
        print("\n====REMOVER EVENTOS OPÇÕES====")
        print("0. Voltar")
        print("\n----EVENTOS PARA REMOVER----")
        listar_eventos()

        if not lista_eventos:
            print("Nenhum evento cadastrado")
            return
        
        
        try:
            remover_id = int(input("Digite o ID do evento para remover: "))
        except ValueError:
            print("ID inválido, digite apenas números: ")
            return
        
        if remover_id == 0:
            return
        
        for evento in lista_eventos:
            if evento['id'] == remover_id:
                lista_eventos.remove(evento)
                print(f"Evento {evento['nome']} removido")
                return



def editar_evento():
    while True:
        print("\n===EDITAR EVENTO OPÇÕES===")
        print("0. Voltar")

        if not lista_eventos:
            print("\nNenhum evento cadastrado")
            return
        
        print("\n---EVENTOS DISPONÍVEIS----")
        listar_eventos()

        try:
            editar_id = int(input("\nDigite o ID do evento para editar: "))
        except ValueError:
            print("ID inválido, digite apenas números: ")
        
        if editar_id == 0:
            return

        for evento in lista_eventos:
            if evento['id'] == editar_id:
                
                print(f"\nEditando Evento ID: {evento['id']} // Nome: {evento['nome']}")
                
                lista_editada = {}

                novo_tema = input(f"Tema atual: {evento['tema']} // Digite um novo tema: ").strip() #DEVO CRIAR FUNÇÃO
                if novo_tema == '0':
                    return
                if novo_tema != '':
                    lista_editada["tema"] = novo_tema
                

                novo_nome = input(f"Nome atual: {evento['tema']} // Digite um novo nome: ").strip() #DEVO CRIAR FUNÇÃO
                if novo_nome == '0':
                    return
                if novo_nome != '':
                    lista_editada["nome"] = novo_nome


                editar_data = input(f"Data atual: {evento['data']} // Quer alterar a data | [s] -> prosseguir [ENTER] -> ignorar: ").strip().lower() #DEVO CRIAR FUNÇÃO
                if editar_data == '0':
                    return
                
                elif editar_data == 's':
                    nova_data = ler_data()
                    if nova_data is None:
                        print("Edição cancelada.")
                        return
                    lista_editada["data"] = nova_data

                elif editar_data == '':
                    print("Data mantida sem alterações.")
                else:
                    print("Opção inválida, edição cancelada.")
                    return               
                

                if lista_editada:
                    evento.update(lista_editada)
                    print(f"\nID: {evento['id']} // Evento: {evento['nome']}' editado!")
                else:
                    print("Nenhuma alteração foi feita no evento.")
                    return
                break
        else:
            print(f"Evento inexistente com o ID: {editar_id}.")


def agrupar_evento(): pass