from eventos import *


def gerenciar_eventos_menu(): 
    while True:
        print("\n===GERENCIAR EVENTOS===")
        print("1. Listar eventos")
        print("2. Buscar evento")
        print("3. Adicionar evento")
        print("4. Remover evento")
        print("5. Editar evento")
        print("0. Voltar")

        opcoes = {
            
                "1": listar_eventos,
                "2": buscar_evento_menu,
                "3": adicionar_evento, 
                "4": remover_evento,
                "5": editar_evento,
            }

        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        elif opcao == "0":
            return
        else:
            print(f"\n {opcao} é uma opção inválida")

def buscar_evento_menu():
    while True:
        print("\n===BUSCAR EVENTO===")
        print("1. Buscar por tema")
        print("2. Buscar por nome")
        print("3. Buscar por data")
        print("0. Voltar")

        opcoes = {
            "1": buscar_por_tema,
            "2": buscar_por_nome,
            "3": buscar_por_data,
        }

        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        elif opcao == "0":
            return
        else:
            print(f"\n {opcao} é uma opção inválida")