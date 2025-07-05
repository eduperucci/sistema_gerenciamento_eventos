from menu_eventos import gerenciar_eventos_menu
from menu_participantes import gerenciar_participantes_menu
from menu_relatorios import analisar_relatorios_menu
from util import limpar_tela


def menu_principal():
    while True:
        limpar_tela()
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
            print("Opção inválida")


def opcao_sair():
    exit()