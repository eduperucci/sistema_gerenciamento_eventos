from eventos import *

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