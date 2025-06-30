from eventos import *
from participantes import *
from relatorios import *

def opcao_sair():
    exit()

def menu_principal():
    while True:
        print("\n====SISTEMA DE GERENCIAMENTO DE EVENTOS===") 
        print("1. Gerenciar eventos")
        print("2. Gerenciar participantes")
        print("3. Analisar relatórios")
        print("0. Sair")

        opcoes = {
            
                "1": gerenciar_eventos_menu,
                "2": gerenciar_participantes_menu, 
                "3": analisar_relatorios_menu,
                "0": opcao_sair,
            }

        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        else:
            print("\nDigite uma opção: ")



def gerenciar_eventos_menu(): 
    while True:
        print("\n===GERENCIAR EVENTOS===")
        print("1. Listar eventos")
        print("2. Adicionar evento")
        print("3. Remover evento")
        print("4. Editar evento")
        print("5. Agrupar eventos")
        print("0. Voltar")

        opcoes = {
            
                "1": listar_eventos,
                "2": adicionar_evento, 
                "3": remover_evento,
                "4": editar_evento,
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
            
                "1": lista_participantes,
                "2": buscar_participante, 
                "3": adicionar_evento,
                "4": editar_evento,
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



def analisar_relatorios_menu():
    while True:
        print("\n===ANALISAR RELATÓRIOS===")
        print("1. Frequência dos Temas")
        print("2. Taxa de participação")
        print("3. Participantes mais ativos")
        print("0. Voltar")

        opcoes = {
            
                "1": temas_frequentes,
                "2": taxa_de_participacao, 
                "3": participantes_mais_ativos,
            }
        
        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        elif opcao == "0":
            return
        else:
            print(f"\n {opcao} é uma opção inválida")


menu_principal()