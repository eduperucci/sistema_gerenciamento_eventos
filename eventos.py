from dados import lista_eventos, lista_de_participantes, salvar_dados, EVENTOS_FILE
from util_eventos import *
from util import ler_data, enter_continuar, limpar_tela

corrigir_id_duplicados(lista_eventos)


def listar_eventos_opcoes():
    limpar_tela()
    print("\n---EVENTOS DISPONÍVEIS---")
    for evento in lista_eventos:
        print(f"ID: {evento['id']} | TEMA: {evento['tema']} | NOME: {evento['nome']} | DATA: {evento['data']}")
    if not lista_eventos:
        print("\nNenhum evento cadastrado")
    enter_continuar()

def listar_eventos():
    limpar_tela()
    print("\n---EVENTOS DISPONÍVEIS---")
    for evento in lista_eventos:
        print(f"ID: {evento['id']} | TEMA: {evento['tema']} | NOME: {evento['nome']} | DATA: {evento['data']}")
    if not lista_eventos:
        print("\nNenhum evento cadastrado")


def adicionar_evento():
    while True:
        limpar_tela()
        print("\n---ADICIONAR EVENTOS---")


        tema_dig = input("Digite o tema do evento ou [0] para cancelar: ")
        if tema_dig == '0':
            return
        

        nome_dig = input("Digite o nome do evento ou [0] para cancelar: ")
        if nome_dig == '0':
            return

        data_dig = ler_data()

        if eventos_na_mesma_data(tema_dig, nome_dig, data_dig, lista_eventos):
            print("\nJá está definido um evento igual nessa data, tente outra data")
            continue

        id_gerado = gerar_id(lista_eventos)


        eventos = {
            "id": id_gerado,    
            "tema": tema_dig,
            "nome": nome_dig,
            "data": data_dig,
            "participantes": []
        }
        
        lista_eventos.append(eventos)
        salvar_dados(EVENTOS_FILE, lista_eventos)
        print(f"\nEvento {nome_dig} criado com sucesso.")
        enter_continuar()
        return


def remover_evento():
    while True:
        limpar_tela()
        print("\n---REMOVER EVENTOS---")
        listar_eventos()

        if not lista_eventos:
            print("Nenhum evento cadastrado")
            enter_continuar()
            return
        
        try:
            remover_id = int(input("Digite o ID do evento para remover ou [0] para cancelar: "))
        except ValueError:
            print("ID inválido, digite apenas números: ")
            enter_continuar()
            continue
        
        if remover_id == 0:
            return
        
        for evento in lista_eventos:
            if evento['id'] == remover_id:
                lista_eventos.remove(evento)
                salvar_dados(EVENTOS_FILE, lista_eventos)
                print(f"Evento {evento['nome']} removido")
                enter_continuar()
                return


def editar_evento():
    while True:
        limpar_tela()
        if not lista_eventos:
            print("\nNenhum evento cadastrado")
            enter_continuar()
            return
        
        print("\n---EVENTOS DISPONÍVEIS----")
        print("0. Voltar")
        listar_eventos()

        try:
            editar_id = int(input("\nDigite o ID do evento para editar ou [0] para voltar: "))
        except ValueError:
            print("ID inválido, digite apenas números: ")
            enter_continuar()
            continue
        
        if editar_id == 0:
            return

        for evento in lista_eventos:
            if evento['id'] == editar_id:
                
                print(f"\nEditando Evento ID: {evento['id']} | Nome: {evento['nome']}")
                
                lista_editada = {}

                novo_tema = input(f"Tema atual: {evento['tema']} | Digite um novo tema [0] para cancelar: ").strip()
                if novo_tema == '0':
                    return
                elif novo_tema != '':
                    lista_editada["tema"] = novo_tema
                

                novo_nome = input(f"Nome atual: {evento['tema']} | Digite um novo nome ou [0] para cancelar: ").strip()
                if novo_nome == '0':
                    return
                if novo_nome != '':
                    lista_editada["nome"] = novo_nome


                editar_data = input(f"Data atual: {evento['data']} | Quer alterar a data | [s] sim para proseguir [ENTER] mandar [0] cancelar: ").strip().lower()
                if editar_data == '0':
                    return
                
                elif editar_data == 's':
                    nova_data = ler_data()
                    if nova_data is None:
                        print("Edição cancelada.")
                        enter_continuar()
                        return
                    lista_editada["data"] = nova_data

                elif editar_data == '':
                    print("Data mantida sem alterações.")
                else:
                    print("Opção inválida, edição cancelada.")
                    enter_continuar()
                    return               
                

                if lista_editada:
                    evento.update(lista_editada)
                    salvar_dados(EVENTOS_FILE, lista_eventos) # Adicione esta linha
                    print(f"\nID: {evento['id']} | Evento: {evento['nome']}' editado!")
                    enter_continuar()
                else:
                    print("Nenhuma alteração foi feita no evento.")
                    enter_continuar()
                    return
                break
        else:
            print(f"Evento inexistente com o ID: {editar_id}.")
            enter_continuar()