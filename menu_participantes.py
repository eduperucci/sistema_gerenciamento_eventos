from participantes import *

def gerenciar_participantes_menu():
    while True:
        print("\n===GERENCIAR PARCIPANTES===")
        print("1. Listar participantes")
        print("2. Buscar participante")
        print("3. Adicionar participante")
        print("4. Remover participante")
        print("5. Editar dados do participante")
        print("0. Voltar")

        opcoes = {
            
                "1": listar_participantes,
                "2": buscar_participante_menu, 
                "3": adicionar_participante,
                "4": remover_participante,
                "5": agrupar_evento,
            }
        
        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        elif opcao == "0":
            return
        else:
            print(f"\n {opcao} é uma opção inválida")


def buscar_participante_menu():
    while True:
        print("===\nBuscar participante===")
        print("1. Buscar por CPF")
        print("2. Buscar por nome")
        print("3. Buscar por email")
        print("0. voltar")

        opcoes = {
            "1": buscar_por_cpf,
            "2": buscar_por_nome,
            "3": buscar_por_email,
        }

        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        elif opcao == "0":
            return
        else:
            print(f"\n {opcao} é uma opção inválida")