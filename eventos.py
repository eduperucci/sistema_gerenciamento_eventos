from dados import lista_eventos
from util import ler_data, gerar_id, corrigir_id_duplicados
from funcoes_eventos import eventos_na_mesma_data

corrigir_id_duplicados(lista_eventos)


def listar_eventos():
    print("\n====EVENTOS DISPONÍVEIS====")
    for evento in lista_eventos:
        print(f"ID: {evento['id']} // TEMA: {evento['tema']} // NOME: {evento['nome']} // DATA: {evento['data']}")
    if not lista_eventos:
        print("\nNenhum evento cadastrado")


def adicionar_evento():
    while True:
        print("\n====ADICIONAR EVENTOS OPÇÕES====")
        print("0. Voltar\n")

        #Adicionar tema do evento
        tema_dig = input("Digite o tema do evento: ")
        if tema_dig == '0':
            return
        
        #Adicionar nome do evento
        nome_dig = input("Digite o nome do evento: ")
        if nome_dig == '0':
            return

        data_dig = ler_data()

        if eventos_na_mesma_data(tema_dig, nome_dig, data_dig, lista_eventos):
            print("\nJá está definido um evento igual nessa data, tente outra data")
            continue

        id_gerado = gerar_id(lista_eventos)

        #Keus e valores dos eventos
        eventos = {
            "id": id_gerado,    
            "tema": tema_dig,
            "nome": nome_dig,
            "data": data_dig  
        }
        
        #Armazena os eventos em uma lista
        lista_eventos.append(eventos)
        print(f"\nEvento {nome_dig} criado com sucesso.")
        return


def remover_evento():
    while True:
        print("\n====REMOVER EVENTOS OPÇÕES====")
        print("0. Voltar\n")

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
                elif novo_tema != '':
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