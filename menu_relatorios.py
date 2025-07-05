from relatorios import *
from util import limpar_tela

def analisar_relatorios_menu():
    while True:
        limpar_tela()
        print("\n===ANALISAR RELATÓRIOS===")
        print("1. Participantes por tema")
        print("2. Participantes por evento")
        print("0. Voltar")

        opcoes = {
            
                "1": participantes_por_tema,
                "2": participantes_por_evento,
            }
        
        opcao = input("\nDigite uma opção: ") 

        acao = opcoes.get(opcao)

        if acao:
            acao()
        elif opcao == "0":
            return
        else:
            print(f"\n {opcao} é uma opção inválida")