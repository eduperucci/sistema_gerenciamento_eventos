from relatorios import *

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